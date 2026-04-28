"""DeepSeek 异步翻译客户端."""

import asyncio
import os

from openai import AsyncOpenAI, APIError, APITimeoutError


class DeepseekTranslate:
    """基于 DeepSeek API 的 Markdown 文本翻译器.

    支持通过 asyncio 并发调用，内部由调用方控制并发量（Semaphore）。
    """

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com",
            timeout=600,  # DeepSeek 请求最长排队 10 分钟
        )
        self.system_prompt = (
            "你是一位专业的学术翻译助手，负责将英文学术论文的 Markdown 文本翻译为中文。"
            "\n"
            "\n## 任务"
            "\n将用户提供的 Markdown 文本中的英文自然语言翻译成地道、流畅的中文学术表达。"
            ""
            "\n"
            "\n## 保留规则（原文照抄，不翻译）"
            "\n翻译时，以下元素必须原封不动保留，仅翻译其周围的自然语言："
            "\n- 数学公式、LaTeX 命令、代码块、行内代码"
            "\n- 引用标注（如 [1]、(Author, 2020)、[2,3] 等）"
            "\n- 正文中的图表引用（如 'see Figure 1'）保留英文；图片 caption 中的 Figure/Table 可译为图/表"
            "\n- URL、DOI、邮箱、文件路径"
            "\n- 人名、机构名、地名"
            "\n- 已约定俗成的算法/模型/数据集/框架名（如 Transformer、ImageNet、PyTorch）"
            "\n- 专有缩写首次出现时保留英文并附中文释义，后续可用中文"
            "\n- Markdown 图片语法中的路径必须保留，alt 文字可译"
            "\n"
            "\n## 翻译规范"
            "\n1. 语言风格：规范的学术中文，逻辑严密、行文流畅，避免口语化。"
            "\n2. 术语统一：同一术语全文翻译一致。"
            "\n3. 语序调整：在准确传达原意的前提下，允许适当调整语序以符合中文习惯。"
            "\n4. 加粗规则：仅对核心概念、关键结论或重要术语使用 **加粗**，每段不超过 2 处。"
            "\n5. 章节标题：翻译为简洁、准确的中文标题。"
            "\n"
            "\n## 重要约束"
            "\n- 必须翻译文本中的全部自然语言内容，不得跳过任何段落或句子。"
            "\n- 如果段落中包含大量保留元素，请翻译其中的自然语言部分，保留非自然语言元素，不要省略整段。"
            "\n- 只输出翻译后的 Markdown 文本，不要添加前言、后注、解释或 ```markdown 代码块。"
            "\n- 保持原有的空行、缩进和换行结构。"
        )

    async def _translate_chunk(self, text: str) -> str:
        """翻译单个子块，带指数退避重试."""
        last_exc = None
        for attempt in range(3):
            try:
                response = await self.client.chat.completions.create(
                    model="deepseek-v4-flash",
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": text},
                    ],
                    temperature=0.3,
                    stream=False,
                )
                return response.choices[0].message.content or ""
            except (APIError, APITimeoutError) as exc:
                last_exc = exc
                if attempt < 2:
                    status_code = getattr(exc, "status_code", None)
                    delay = 10 if status_code == 429 else 2 * (attempt + 1)
                    await asyncio.sleep(delay)
        raise last_exc  # type: ignore[misc]

    async def get_result(self, text: str) -> str:
        """异步翻译单段 Markdown 文本.

        Args:
            text: 待翻译的 Markdown 文本.

        Returns:
            翻译后的字符串。若 API 返回空内容则返回空字符串。

        Raises:
            APIError: 当 DeepSeek API 返回非 2xx 或网络异常时抛出.
        """
        return await self._translate_chunk(text)
