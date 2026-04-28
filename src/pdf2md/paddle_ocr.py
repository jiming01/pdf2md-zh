"""PaddleOCR-VL-1.5 API 客户端（同步 HTTP 轮询）."""

import os
import json
import time
from typing import Callable, TypeVar

import requests

from .logger import console

T = TypeVar("T")


def _retry_request(
    func: Callable[[], T],
    max_retries: int = 3,
    delay: float = 2.0,
    backoff: float = 2.0,
    label: str = "请求",
) -> T:
    """带指数退避的重试包装器，用于处理瞬态网络错误."""
    last_exc = None
    current_delay = delay
    for attempt in range(max_retries + 1):
        try:
            return func()
        except requests.RequestException as exc:
            last_exc = exc
            if attempt < max_retries:
                console.print(
                    f"[yellow]⚠ {label}失败，{current_delay:.0f}s 后重试 "
                    f"({attempt + 1}/{max_retries}): {exc}[/yellow]"
                )
                time.sleep(current_delay)
                current_delay *= backoff
    raise last_exc  # type: ignore[misc]


class PaddleOCR:
    """调用百度飞桨 AI Studio 的 PaddleOCR-VL-1.5 API 进行 PDF 结构提取.

    整个 OCR 流程为阻塞式同步调用：提交任务 → 轮询状态 → 下载结果。
    调用方如需在 async 上下文中使用，请自行通过 ``asyncio.to_thread`` 包装.
    """

    def __init__(self) -> None:
        self.api_url = "https://paddleocr.aistudio-app.com/api/v2/ocr/jobs"
        self.token = os.getenv("PADDLE_API_TOKEN")
        if not self.token:
            raise RuntimeError("环境变量 PADDLE_API_TOKEN 未设置，请检查 .env 文件")

        self.model = "PaddleOCR-VL-1.5"
        self.headers = {
            "Authorization": f"bearer {self.token}",
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

    def get_result(self, file_path: str):
        """提交 PDF 并轮询获取 OCR 结果（JSONL 格式）.

        Args:
            file_path: 本地 PDF 文件路径.

        Returns:
            结果 JSONL 按行切分后的字符串列表.

        Raises:
            FileNotFoundError: 当 ``file_path`` 不存在时.
            RuntimeError: 当 API 提交失败或任务执行失败时.
            requests.HTTPError: 当下载结果文件失败时.
        """
        # 1. 校验文件存在性
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        # 2. 提交 OCR 任务
        data = {
            "model": self.model,
            "optionalPayload": json.dumps(self.optional_payload),
        }

        def _submit_job():
            with open(file_path, "rb") as f:
                return requests.post(
                    self.api_url,
                    headers=self.headers,
                    data=data,
                    files={"file": f},
                    timeout=60,
                )

        try:
            job_response = _retry_request(_submit_job, label="提交 PaddleOCR 任务")
        except requests.RequestException as exc:
            raise RuntimeError(f"提交 PaddleOCR 任务失败: {exc}") from exc

        if job_response.status_code != 200:
            raise RuntimeError(
                f"PaddleOCR 任务提交失败，状态码 {job_response.status_code}"
            )

        job_id = job_response.json()["data"]["jobId"]

        # 3. 轮询结果（使用 spinner 展示状态）
        jsonl_url = ""
        with console.status("[bold green]OCR 处理中...[/bold green]") as status:
            while True:
                try:
                    job_result_response = _retry_request(
                        lambda: requests.get(
                            f"{self.api_url}/{job_id}",
                            headers=self.headers,
                            timeout=30,
                        ),
                        label="轮询 PaddleOCR 状态",
                    )
                except requests.RequestException as exc:
                    raise RuntimeError(f"轮询 PaddleOCR 任务状态失败: {exc}") from exc

                if job_result_response.status_code != 200:
                    raise RuntimeError(
                        f"轮询 PaddleOCR 任务状态失败，状态码 {job_result_response.status_code}"
                    )

                resp_data = job_result_response.json()["data"]
                state = resp_data["state"]

                if state == "pending":
                    status.update("[bold yellow]OCR 排队中...[/bold yellow]")
                elif state == "running":
                    try:
                        total_pages = resp_data["extractProgress"]["totalPages"]
                        extracted_pages = resp_data["extractProgress"]["extractedPages"]
                        status.update(
                            f"[bold green]OCR 提取中... {extracted_pages}/{total_pages} 页"
                            f"[/bold green]"
                        )
                    except KeyError:
                        status.update("[bold green]OCR 提取中...[/bold green]")
                elif state == "done":
                    extracted_pages = resp_data["extractProgress"]["extractedPages"]
                    console.log(
                        f"[green]✓ OCR 完成，共提取 {extracted_pages} 页[/green]"
                    )
                    jsonl_url = resp_data["resultUrl"]["jsonUrl"]
                    break
                elif state == "failed":
                    error_msg = resp_data.get("errorMsg", "未知错误")
                    raise RuntimeError(f"PaddleOCR 任务执行失败: {error_msg}")

                time.sleep(5)

        # 4. 下载并返回结果
        if not jsonl_url:
            raise RuntimeError("PaddleOCR 任务已完成但未返回结果 URL")

        try:
            jsonl_response = _retry_request(
                lambda: requests.get(jsonl_url, timeout=60),
                label="下载 OCR 结果",
            )
            jsonl_response.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"下载 OCR 结果失败: {exc}") from exc

        lines = jsonl_response.text.strip().split("\n")
        return lines
