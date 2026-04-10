# ocr 与 翻译整合
import os

import requests

from .deepseek_trans import DeekseekTranslate
from .paddle_ocr import PaddleOCR


class PDF2MD:
    def __init__(self, input_path, output_path) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.ocr_model = PaddleOCR()
        self.trans_model = DeekseekTranslate()

    def pdf2md(self):

        # 得到 ocr 结果
        result = self.ocr_model.get_result(self.input_path)
        # ocr 结果写入文件
        for i, res in enumerate(result["layoutParsingResults"]):
            # 保存文本
            md_filename = os.path.join(self.output_path, f"doc_{i}.md")
            with open(md_filename, "w") as md_file:
                text = res["markdown"]["text"]
                trans_text = self.trans_model.get_result(text)
                md_file.write(text)
                md_file.write("\n")
                md_file.write(trans_text)
            print(f"Markdown document saved at {md_filename}")

            # 保存图片
            for img_path, img in res["markdown"]["images"].items():
                full_img_path = os.path.join(self.output_path, img_path)
                os.makedirs(os.path.dirname(full_img_path), exist_ok=True)
                img_bytes = requests.get(img).content
                with open(full_img_path, "wb") as img_file:
                    img_file.write(img_bytes)
                print(f"Image saved to: {full_img_path}")

            for img_name, img in res["outputImages"].items():
                img_response = requests.get(img)
                if img_response.status_code == 200:
                    # Save image to local
                    layout_path = os.path.join(self.output_path, "layout")
                    os.makedirs(layout_path, exist_ok=True)
                    filename = os.path.join(layout_path, f"{img_name}_{i}.jpg")
                    with open(filename, "wb") as f:
                        f.write(img_response.content)
                    print(f"Image saved to: {filename}")
                else:
                    print(
                        f"Failed to download image, status code: {img_response.status_code}"
                    )
