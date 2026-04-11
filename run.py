import os
import asyncio
from pathlib import Path
from pdf2md.pdf2md import PDF2MD


async def main():
    input_path = "./pdf/paper.pdf"
    basename = Path(input_path).stem
    output_path = os.path.join("./md", basename)
    os.makedirs(output_path, exist_ok=True)

    agent = PDF2MD(input_path, output_path, combine_page=50, trans_num=10)
    await agent.pdf2md()


if __name__ == "__main__":
    asyncio.run(main())
