"""PDF2MD 编排器：OCR 提取 → 翻译 → 分页合并."""

import asyncio
import json
import math
import os
import re

import requests
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

from .deepseek_trans import DeepseekTranslate
from .paddle_ocr import PaddleOCR
from .logger import console


# 注入到合并后 Markdown 的学术排版 CSS 样式
STYLE = """<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&display=swap');
body, .markdown-preview, .mume {
    font-family: 'Lora', serif !important;
    font-size: 17px !important;
    line-height: 1.7 !important;
    color: #333333 !important;
}
h1, h2, h3, h4, h5, h6 {
    font-family: inherit !important;
    font-weight: bold !important;
    color: #000000 !important;
    margin-top: 1.5em !important;
    margin-bottom: 0.5em !important;
}
p { text-align: justify !important; }
</style>\n\n"""


class PDF2MD:
    """将 PDF 转为 Markdown，支持仅 OCR 或 OCR+翻译两种模式.

    Attributes:
        input_path: 输入 PDF 文件路径.
        output_path: 输出目录路径.
        combine_page: 每组合并的页数（默认 50）.
        trans_num: 翻译最大并发数（默认 10）.
    """

    def __init__(
        self,
        input_path: str,
        output_path: str,
        combine_page: int = 50,
        trans_num: int = 10,
    ) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.combine_page = combine_page
        self.trans_num = trans_num
        self.ocr_model = PaddleOCR()
        self.trans_model = DeepseekTranslate()

    # ------------------------------------------------------------------ #
    #  页面解析（从 OCR 返回的 JSONL 中提取 layoutParsingResults）
    # ------------------------------------------------------------------ #
    def _parse_pages(self, lines: list[str]) -> list[dict]:
        """从 PaddleOCR 返回的 JSONL 行列表中解析页面数据.

        Args:
            lines: JSONL 按行拆分后的字符串列表.

        Returns:
            页面字典列表，每个字典包含 ``markdown`` 键.
        """
        pages: list[dict] = []
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                result = json.loads(line)["result"]
                pages.extend(result["layoutParsingResults"])
            except (json.JSONDecodeError, KeyError) as exc:
                console.print(
                    f"[yellow]⚠ 解析第 {line_num} 行 OCR 结果失败，已跳过: {exc}[/yellow]"
                )
        return pages

    # ------------------------------------------------------------------ #
    #  Markdown 后处理（公式、换行）
    # ------------------------------------------------------------------ #
    def _re_process(self, text: str) -> str:
        """修复公式渲染格式问题.

        - 去除行内公式 ``$ ... $`` 中的多余空格.
        - 规范化块级公式 ``$$...$$`` 的换行.
        - 压缩连续三个以上换行为两个.

        Args:
            text: 原始 Markdown 文本.

        Returns:
            处理后的文本（不修改原始输入）.
        """
        # $ {formula} $ -> ${formula}$
        text = re.sub(r"(?<!\$)\$\s+([^$]+?)\s+\$(?!\$)", r"$\1$", text)

        # $$...$$ -> 独立成块并去除首尾空白
        text = re.sub(
            r"\$\$([\s\S]*?)\$\$",
            lambda m: f"\n$$\n{m.group(1).strip()}\n$$\n",
            text,
            flags=re.MULTILINE,
        )

        # 连续三个以上换行压缩为两个
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text

    # ------------------------------------------------------------------ #
    #  文件排序与合并
    # ------------------------------------------------------------------ #
    def _extract_page_index(self, filename: str) -> int:
        """从 ``doc_{index}.md`` 或 ``doc_{index}_trans.md`` 中提取页码索引.

        Args:
            filename: 中间文件名.

        Returns:
            提取到的页码数字；若提取失败返回 -1.
        """
        match = re.search(r"(\d+)", filename)
        return int(match.group(1)) if match else -1

    def _combine_page(
        self, prefix: str = "doc", suffix: str = ".md", out_prefix: str = "group"
    ) -> None:
        """将中间文件按页数合并为分组 Markdown，并生成完整版.

        合并完成后会删除原始中间文件.

        Args:
            prefix: 中间文件前缀，如 ``doc``.
            suffix: 中间文件后缀，如 ``.md`` 或 ``_trans.md``.
            out_prefix: 输出文件前缀，如 ``group`` 或 ``group_trans``.
        """
        pattern = re.compile(rf"^{re.escape(prefix)}_\d+{re.escape(suffix)}$")
        files = [f for f in os.listdir(self.output_path) if pattern.match(f)]
        files.sort(key=self._extract_page_index)

        total = len(files)
        if total == 0:
            console.print("[yellow]⚠ 未找到可合并的中间文件[/yellow]")
            return

        num_groups = math.ceil(total / self.combine_page)

        # 生成分组文件
        for group_idx in range(num_groups):
            start = group_idx * self.combine_page
            end = min(start + self.combine_page, total)
            group_files = files[start:end]

            out_filename = os.path.join(
                self.output_path, f"{out_prefix}_{group_idx}{suffix}"
            )
            with open(out_filename, "w", encoding="utf-8") as out_f:
                out_f.write(STYLE)
                for i, fname in enumerate(group_files):
                    file_path = os.path.join(self.output_path, fname)
                    with open(file_path, "r", encoding="utf-8") as in_f:
                        out_f.write(in_f.read())
                    if i < len(group_files) - 1:
                        out_f.write("\n\n---\n\n")

        # 生成完整版合并文件
        full_filename = os.path.join(self.output_path, f"{out_prefix}_full{suffix}")
        with open(full_filename, "w", encoding="utf-8") as full_f:
            full_f.write(STYLE)
            for i, fname in enumerate(files):
                file_path = os.path.join(self.output_path, fname)
                with open(file_path, "r", encoding="utf-8") as in_f:
                    full_f.write(in_f.read())
                if i < len(files) - 1:
                    full_f.write("\n\n---\n\n")

        # 清理中间文件
        for f in files:
            os.remove(os.path.join(self.output_path, f))

    # ------------------------------------------------------------------ #
    #  中间文件清理（异常回滚用）
    # ------------------------------------------------------------------ #
    def _cleanup_intermediate_files(self) -> None:
        """清理异常后残留的中间 Markdown 文件，包括 doc 和 group 开头的."""
        if not os.path.isdir(self.output_path):
            return
        patterns = (
            re.compile(r"^doc_\d+\.md$"),
            re.compile(r"^doc_\d+_trans\.md$"),
            re.compile(r"^group_\d+\.md$"),
            re.compile(r"^group_full\.md$"),
            re.compile(r"^group_trans_\d+_trans\.md$"),
            re.compile(r"^group_trans_full_trans\.md$"),
        )
        count = 0
        for f in os.listdir(self.output_path):
            if any(p.match(f) for p in patterns):
                try:
                    os.remove(os.path.join(self.output_path, f))
                    count += 1
                except OSError:
                    pass
        if count:
            console.print(f"[yellow]⚠ 已清理 {count} 个残留中间文件[/yellow]")

    # ------------------------------------------------------------------ #
    #  图片保存（同步 & 异步）
    # ------------------------------------------------------------------ #
    def _download_image(self, img_path: str, img_url: str) -> bool:
        """下载单张图片到 ``output_path``，已存在则跳过.

        Args:
            img_path: 相对路径（如 ``images/foo.png``）.
            img_url: 远程 URL.

        Returns:
            ``True`` 表示成功或已存在.
        """
        full_img_path = os.path.join(self.output_path, img_path)
        if os.path.exists(full_img_path):
            return True
        os.makedirs(os.path.dirname(full_img_path), exist_ok=True)
        try:
            resp = requests.get(
                img_url, timeout=30, headers={"User-Agent": "pdf2md/0.1.0"}
            )
            resp.raise_for_status()
            with open(full_img_path, "wb") as img_file:
                img_file.write(resp.content)
            return True
        except Exception as exc:
            console.print(f"[yellow]⚠ 图片下载失败 {img_url}: {exc}[/yellow]")
            return False

    def _save_images_sync(self, images: dict[str, str]) -> int:
        """同步下载并保存单页图片.

        Args:
            images: ``{相对路径: URL}`` 映射.

        Returns:
            成功下载的图片数量.
        """
        success_count = 0
        for img_path, img_url in images.items():
            if self._download_image(img_path, img_url):
                success_count += 1
        return success_count

    async def _save_all_images_async(self, images: dict[str, str]) -> int:
        """跨页异步并发下载所有图片（线程池）.

        Args:
            images: ``{相对路径: URL}`` 映射（已预收集，跨所有页面）.

        Returns:
            成功下载的图片数量.
        """
        if not images:
            return 0
        results = await asyncio.gather(
            *[
                asyncio.to_thread(self._download_image, img_path, img_url)
                for img_path, img_url in images.items()
            ],
            return_exceptions=True,
        )
        return sum(1 for r in results if r is True)

    # ------------------------------------------------------------------ #
    #  页面写入（同步 & 异步）
    # ------------------------------------------------------------------ #
    def _pure_write_page(self, pages: list[dict]) -> None:
        """同步保存原始 OCR 文本和图片（供 ``pure_pdf2md`` 使用）.

        Args:
            pages: OCR 解析后的页面列表.
        """
        processed_texts = [self._re_process(page["markdown"]["text"]) for page in pages]
        total = len(pages)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("保存页面", total=total)

            for i, (page_data, text) in enumerate(zip(pages, processed_texts)):
                md_filename = os.path.join(self.output_path, f"doc_{i}.md")
                with open(md_filename, "w", encoding="utf-8") as md_file:
                    md_file.write(text)

                img_count = self._save_images_sync(page_data["markdown"]["images"])
                progress.update(
                    task,
                    advance=1,
                    description=f"保存页面 (第 {i + 1}/{total} 页)",
                )
                if img_count:
                    progress.update(
                        task,
                        description=f"保存页面 (第 {i + 1}/{total} 页, 图片 {img_count} 张)",
                    )

        console.print(f"[green]✓ 已保存 {total} 页 Markdown 及配图[/green]")

    async def _async_write_pages(self, pages: list[dict]) -> None:
        """异步保存原始 OCR 文本和图片（供 ``pdf2md`` 使用）.

        先写入全部 Markdown 文件，再跨页并发下载所有图片，
        避免页级串行阻塞.

        Args:
            pages: OCR 解析后的页面列表.
        """
        processed_texts = [self._re_process(page["markdown"]["text"]) for page in pages]
        total = len(pages)

        # 1) 写入所有 Markdown 文件
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("保存页面", total=total)
            for i, text in enumerate(processed_texts):
                md_filename = os.path.join(self.output_path, f"doc_{i}.md")
                with open(md_filename, "w", encoding="utf-8") as md_file:
                    md_file.write(text)
                progress.update(
                    task,
                    advance=1,
                    description=f"保存页面 (第 {i + 1}/{total} 页)",
                )

        # 2) 预收集全部图片并跨页并发下载
        all_images: dict[str, str] = {}
        for page_data in pages:
            all_images.update(page_data["markdown"]["images"])
        if all_images:
            img_count = await self._save_all_images_async(all_images)
            console.print(
                f"[green]✓ 已保存 {total} 页 Markdown 及 {img_count} 张配图[/green]"
            )
        else:
            console.print(f"[green]✓ 已保存 {total} 页 Markdown[/green]")

    # ------------------------------------------------------------------ #
    #  翻译写入
    # ------------------------------------------------------------------ #
    async def _write_trans_page(self, pages: list[dict]) -> None:
        """异步并行翻译每一页并流式写入 ``doc_{i}_trans.md``.

        通过 Semaphore 限制并发数，避免触发 API 限流。
        若翻译返回空内容或网络异常，降级保留原文，确保输出不丢失内容。

        Args:
            pages: OCR 解析后的页面列表.
        """
        original_texts = [page["markdown"]["text"] for page in pages]
        semaphore = asyncio.Semaphore(self.trans_num)
        total = len(original_texts)

        async def translate_one(text: str, idx: int) -> tuple[int, str]:
            async with semaphore:
                try:
                    result = await self.trans_model.get_result(text)
                except Exception:
                    console.print(f"[yellow]⚠ 第 {idx} 页翻译异常，保留原文[/yellow]")
                    result = ""
            if not result.strip():
                return idx, text
            return idx, result

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            transient=True,
        ) as progress:
            task_id = progress.add_task(
                f"翻译页面 (并发 {self.trans_num})", total=total
            )

            # 创建任务但不立即 gather，以便 as_completed 流式消费
            pending = {
                asyncio.create_task(translate_one(text, i))
                for i, text in enumerate(original_texts)
            }

            while pending:
                done, pending = await asyncio.wait(
                    pending, return_when=asyncio.FIRST_COMPLETED
                )
                for fut in done:
                    idx, trans_text = fut.result()
                    trans_md_filename = os.path.join(
                        self.output_path, f"doc_{idx}_trans.md"
                    )
                    with open(trans_md_filename, "w", encoding="utf-8") as md_file:
                        md_file.write(trans_text)
                    progress.advance(task_id)

        console.print(f"[green]✓ 已完成 {total} 页翻译[/green]")

    # ------------------------------------------------------------------ #
    #  公共 API
    # ------------------------------------------------------------------ #
    async def pdf2md(self) -> None:
        """OCR + 翻译模式.

        流程：OCR 提取 → 保存原文 → 异步翻译 → 合并分组.
        任意步骤失败时会自动清理已生成的中间 Markdown 文件.
        """
        lines = await asyncio.to_thread(self.ocr_model.get_result, self.input_path)
        pages = self._parse_pages(lines)

        try:
            await self._async_write_pages(pages)
            await self._write_trans_page(pages)

            self._combine_page(prefix="doc", suffix=".md", out_prefix="group")
            self._combine_page(
                prefix="doc", suffix="_trans.md", out_prefix="group_trans"
            )
        except Exception:
            self._cleanup_intermediate_files()
            raise

    def pure_pdf2md(self) -> None:
        """仅 OCR 模式（同步阻塞）.

        流程：OCR 提取 → 保存原文 → 合并分组.
        任意步骤失败时会自动清理已生成的中间 Markdown 文件.
        """
        lines = self.ocr_model.get_result(self.input_path)
        pages = self._parse_pages(lines)

        try:
            self._pure_write_page(pages)
            self._combine_page(prefix="doc", suffix=".md", out_prefix="group")
        except Exception:
            self._cleanup_intermediate_files()
            raise
