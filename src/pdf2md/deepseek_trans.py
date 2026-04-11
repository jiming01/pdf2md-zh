import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()


class DeekseekTranslate:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
        )
        self.system_prompt = (
            "将下面 Markdown 文本中的英文自然语言翻译成中文（不翻译术语、人名、引用格式）。"
            "翻译后逻辑严密，语言通顺，行文流畅，符合中文语序"
            "输出格式：每行自然语言翻译前**必须**加字符'>'（块级公式，表格内元素不需要加 > ），保持原有换行和 Markdown 结构。只输出翻译结果，不要原文。"
            "优化：给你认为能够优化阅读体验的字句加粗。比例在5% 左右"
        )

    async def get_result(self, text: str) -> str:
        """异步翻译单段文本"""
        response = await self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": text},
            ],
            temperature=1.3,
        )

        return response.choices[0].message.content or ""
