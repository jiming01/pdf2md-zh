# 使用paddle aistudio 的 PaddleOCR-VL-1.5 API来对 pdf 进行文本结构提取

import base64
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class PaddleOCR:
    def __init__(self) -> None:
        self.api_url = "https://xcz5qad739b8nek1.aistudio-app.com/layout-parsing"
        self.token = os.getenv("PADDLE_API_TOKEN")
        self.headers = {
            "Authorization": f"token {self.token}",
            "Content-Type": "application/json",
        }

    def get_result(self, file_path):
        # 格式转换
        with open(file_path, "rb") as file:
            file_bytes = file.read()
            file_data = base64.b64encode(file_bytes).decode("ascii")

        # 配置
        required_payload = {
            "file": file_data,
            "fileType": 0,  # For PDF documents, set `fileType` to 0; for images, set `fileType` to 1
        }
        optional_payload = {
            "useDocOrientationClassify": False,
            "useDocUnwarping": False,
            "useChartRecognition": False,
            "restructurePages": True,
            "prettifyMarkdown": True,
        }
        payload = {**required_payload, **optional_payload}

        # 获取结果
        response = requests.post(self.api_url, json=payload, headers=self.headers)
        print(response.status_code)
        assert response.status_code == 200
        result = response.json()["result"]

        return result


# 官方API使用示例
"""
# Please make sure the requests library is installed
# pip install requests
import base64
import os
import requests

API_URL = "https://xcz5qad739b8nek1.aistudio-app.com/layout-parsing"
TOKEN = "xxx"

file_path = "<local file path>"

with open(file_path, "rb") as file:
    file_bytes = file.read()
    file_data = base64.b64encode(file_bytes).decode("ascii")

headers = {
    "Authorization": f"token {TOKEN}",
    "Content-Type": "application/json"
}

required_payload = {
    "file": file_data,
    "fileType": <file type>,  # For PDF documents, set `fileType` to 0; for images, set `fileType` to 1
}

optional_payload = {
    "useDocOrientationClassify": False,
    "useDocUnwarping": False,
    "useChartRecognition": False,
}

payload = {**required_payload, **optional_payload}

response = requests.post(API_URL, json=payload, headers=headers)
print(response.status_code)
assert response.status_code == 200
result = response.json()["result"]

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for i, res in enumerate(result["layoutParsingResults"]):
    md_filename = os.path.join(output_dir, f"doc_{i}.md")
    with open(md_filename, "w") as md_file:
        md_file.write(res["markdown"]["text"])
    print(f"Markdown document saved at {md_filename}")
    for img_path, img in res["markdown"]["images"].items():
        full_img_path = os.path.join(output_dir, img_path)
        os.makedirs(os.path.dirname(full_img_path), exist_ok=True)
        img_bytes = requests.get(img).content
        with open(full_img_path, "wb") as img_file:
            img_file.write(img_bytes)
        print(f"Image saved to: {full_img_path}")
    for img_name, img in res["outputImages"].items():
        img_response = requests.get(img)
        if img_response.status_code == 200:
            # Save image to local
            filename = os.path.join(output_dir, f"{img_name}_{i}.jpg")
            with open(filename, "wb") as f:
                f.write(img_response.content)
            print(f"Image saved to: {filename}")
        else:
            print(f"Failed to download image, status code: {img_response.status_code}")
"""
