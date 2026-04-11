# 使用paddle aistudio 的 PaddleOCR-VL-1.5 API来对 pdf 进行文本结构提取

import os
import sys
import json
import time

import requests
from dotenv import load_dotenv

load_dotenv()


class PaddleOCR:
    def __init__(self) -> None:
        self.api_url = "https://paddleocr.aistudio-app.com/api/v2/ocr/jobs"
        self.token = os.getenv("PADDLE_API_TOKEN")
        self.model = "PaddleOCR-VL-1.5"
        self.headers = {
            "Authorization": f"bearer {self.token}",
            # "Content-Type": "application/json",
        }
        self.optional_payload = {
            "useDocOrientationClassify": False,
            "useDocUnwarping": False,
            "useChartRecognition": False,
            "restructurePages": True,
            "prettifyMarkdown": True,
            "showFormulaNumber": True,
            "visualize": False,
        }

    def get_result(self, file_path):
        # 检验文件是否存在
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            sys.exit(1)
        print(f"Processing file: {file_path}")

        # 配置
        data = {
            "model": self.model,
            "optionalPayload": json.dumps(self.optional_payload),
        }

        # 提交任务
        with open(file_path, "rb") as f:
            files = {"file": f}
            job_response = requests.post(
                self.api_url, headers=self.headers, data=data, files=files
            )

        print(f"Response status: {job_response.status_code}")
        if job_response.status_code != 200:
            print(f"Response content: {job_response.text}")

        assert job_response.status_code == 200
        jobId = job_response.json()["data"]["jobId"]
        print(f"Job submitted successfully. job id: {jobId}")
        print("Start polling for results")

        # 轮询结果
        jsonl_url = ""
        while True:
            job_result_response = requests.get(
                f"{self.api_url}/{jobId}", headers=self.headers
            )
            assert job_result_response.status_code == 200
            state = job_result_response.json()["data"]["state"]
            if state == "pending":
                print("The current status of the job is pending")
            elif state == "running":
                try:
                    total_pages = job_result_response.json()["data"]["extractProgress"][
                        "totalPages"
                    ]
                    extracted_pages = job_result_response.json()["data"][
                        "extractProgress"
                    ]["extractedPages"]
                    print(
                        f"The current status of the job is running, total pages: {total_pages}, extracted pages: {extracted_pages}"
                    )
                except KeyError:
                    print("The current status of the job is running...")
            elif state == "done":
                extracted_pages = job_result_response.json()["data"]["extractProgress"][
                    "extractedPages"
                ]
                start_time = job_result_response.json()["data"]["extractProgress"][
                    "startTime"
                ]
                end_time = job_result_response.json()["data"]["extractProgress"][
                    "endTime"
                ]
                print(
                    f"Job completed, successfully extracted pages: {extracted_pages}, start time: {start_time}, end time: {end_time}"
                )
                jsonl_url = job_result_response.json()["data"]["resultUrl"]["jsonUrl"]
                break
            elif state == "failed":
                error_msg = job_result_response.json()["data"]["errorMsg"]
                print(f"Job failed, failure reason:{error_msg}")
                sys.exit()

            time.sleep(5)

        # 返回结果
        if jsonl_url:
            jsonl_response = requests.get(jsonl_url)
            jsonl_response.raise_for_status()
            lines = jsonl_response.text.strip().split("\n")

        return lines
