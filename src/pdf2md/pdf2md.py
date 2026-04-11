# ocr 与 翻译整合
import asyncio
import json
import math
import os
import re

import requests

from .deepseek_trans import DeekseekTranslate
from .paddle_ocr import PaddleOCR


class PDF2MD:
    def __init__(self, input_path, output_path, combine_page=50, trans_num=10) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.combine_page = combine_page
        self.trans_num = trans_num
        self.page_num = 0
        self.ocr_model = PaddleOCR()
        self.trans_model = DeekseekTranslate()

    def _combine_page(self):
        # 获取所有 doc_*.md 文件，按数字索引排序
        files = [
            f
            for f in os.listdir(self.output_path)
            if f.startswith("doc_") and f.endswith(".md")
        ]
        # 按数字排序（doc_0.md, doc_1.md, ...）
        files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

        total = len(files)
        if total == 0:
            print("没有找到 doc_*.md 文件")
            return

        # 计算需要多少组
        num_groups = math.ceil(total / self.combine_page)

        for group_idx in range(num_groups):
            start = group_idx * self.combine_page
            end = min(start + self.combine_page, total)
            group_files = files[start:end]

            out_filename = os.path.join(self.output_path, f"group_{group_idx}.md")
            with open(out_filename, "w", encoding="utf-8") as out_f:
                for i, fname in enumerate(group_files):
                    file_path = os.path.join(self.output_path, fname)
                    with open(file_path, "r", encoding="utf-8") as in_f:
                        content = in_f.read()
                    out_f.write(content)
                    # 如果不是本组的最后一个文件，添加一个分隔线（可选）
                    if i < len(group_files) - 1:
                        out_f.write("\n\n---\n\n")  # 水平分割线
            print(f"已生成: {out_filename} (包含文件 {start}~{end - 1})")

        print(f"完成！共 {total} 个文件，分为 {num_groups} 组。")

        # 请理原有文件
        for f in files:
            file_path = os.path.join(self.output_path, f)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

    def _re_process(self, text):
        """解决公式渲染格式问题"""

        # $ {fomula} $ -> ${fomula}$
        text = re.sub(r"(?<!\$)\$\s+([^$]+?)\s+\$(?!\$)", r"$\1$", text)

        # {indent}$${fomula}$$ -> \n$$\n {fomula} \n$$\n
        text = re.sub(
            r"\$\$([\s\S]*?)\$\$",
            lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n",
            text,
            flags=re.MULTILINE,
        )

        # 多个换行处理
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text

    async def _write_page(self, pages):
        """
        异步并行翻译每一页，最大并发数为 self.trans_num。
        保持原有文件保存和图片下载逻辑（同步）。
        """

        # 提取所有需要翻译的原始文本
        for page in pages:
            page["markdown"]["text"] = self._re_process(page["markdown"]["text"])

        original_texts = [page["markdown"]["text"] for page in pages]

        semaphore = asyncio.Semaphore(self.trans_num)

        async def translate_one(text: str, idx: int) -> str:
            """带信号量限制的单个翻译任务"""
            async with semaphore:
                print(f"Starting translation for page {idx}")
                translated = await self.trans_model.get_result(text)
                print(f"Finished translation for page {idx}")
                return translated

        # 并发执行所有翻译任务，保持顺序
        tasks = [translate_one(text, i) for i, text in enumerate(original_texts)]
        translated_texts = await asyncio.gather(*tasks)

        # 按顺序处理每一页：保存 md 文件 + 下载图片
        for page_data, trans_text in zip(pages, translated_texts):
            # 保存文本
            md_filename = os.path.join(self.output_path, f"doc_{self.page_num}.md")
            with open(md_filename, "w") as md_file:
                text = page_data["markdown"]["text"]
                md_file.write("\n" + text)
                md_file.write("\n" + trans_text)
            print(f"Markdown document saved at {md_filename}")

            # 保存图片
            for img_path, img in page_data["markdown"]["images"].items():
                full_img_path = os.path.join(self.output_path, img_path)
                os.makedirs(os.path.dirname(full_img_path), exist_ok=True)
                img_bytes = requests.get(img).content
                with open(full_img_path, "wb") as img_file:
                    img_file.write(img_bytes)
                print(f"Image saved to: {full_img_path}")

            self.page_num += 1
            ## 版面分析图像，可以不下载
            # for img_name, img in page_data["outputImages"].items():
            #     img_page_dataponse = requests.get(img)
            #     if img_page_dataponse.status_code == 200:
            #         # Save image to local
            #         layout_path = os.path.join(self.output_path, "layout")
            #         os.makedirs(layout_path, exist_ok=True)
            #         filename = os.path.join(layout_path, f"{img_name}_{i}.jpg")
            #         with open(filename, "wb") as f:
            #             f.write(img_page_dataponse.content)
            #         print(f"Image saved to: {filename}")
            #     else:
            #         print(
            #             f"Failed to download image, status code: {img_page_dataponse.status_code}"
            #         )

    async def pdf2md(self):
        # 得到 ocr 结果
        lines = self.ocr_model.get_result(self.input_path)
        # 翻译并写入文件
        pages = []
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue
            result = json.loads(line)["result"]
            pages.extend(result["layoutParsingResults"])

        await self._write_page(pages)
        self._combine_page()
