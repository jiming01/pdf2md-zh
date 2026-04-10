import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class DeekseekTranslate:
    def __init__(self) -> None:
        self.base_url = "https://api.deepseek.com"
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.system_prompt = (
            "将下面 Markdown 文本中的英文自然语言翻译成中文（不翻译术语、人名、引用格式）。"
            "翻译后逻辑严密，语言通顺，行文流畅，符合中文语序"
            "输出格式：每段翻译前加 `> `（表格内元素不需要加 > ），保持原有换行和 Markdown 结构。只输出翻译结果，不要原文。"
        )

    def get_result(self, text):
        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": text},
            ],
            temperature = 1.3,
            stream=False,
        )
        result = response.choices[0].message.content
        return "" if result is None else result


"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)
"""
