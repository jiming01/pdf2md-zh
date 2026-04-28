"""PDF2MD 命令行入口."""

import argparse
import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from pdf2md.pdf2md import PDF2MD
from pdf2md.logger import console

load_dotenv()


def parse_args() -> argparse.Namespace:
    """解析命令行参数."""
    parser = argparse.ArgumentParser(
        description="将 PDF 转为 Markdown，支持 OCR 与翻译"
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="./pdf/DeepSeek_V4.pdf",
        help="输入 PDF 文件路径 (默认: ./pdf/DeepSeek_V4.pdf)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="输出目录路径 (默认: ./md/<pdf文件名>)",
    )
    parser.add_argument(
        "--pure",
        action="store_true",
        help="仅 OCR，不进行翻译",
    )
    parser.add_argument(
        "--combine-page",
        type=int,
        default=50,
        help="每组合并页数 (默认: 50)",
    )
    parser.add_argument(
        "--trans-num",
        type=int,
        default=10,
        help="翻译最大并发数 (默认: 10)",
    )
    return parser.parse_args()


async def main() -> int:
    """主入口协程."""
    args = parse_args()

    input_path = args.input
    if args.output is None:
        basename = Path(input_path).stem
        output_path = os.path.join("./md", basename)
    else:
        output_path = args.output

    os.makedirs(output_path, exist_ok=True)

    console.rule(f"[bold blue]PDF2MD – {Path(input_path).name}[/bold blue]")
    console.print(f"[dim]输出目录: {output_path}[/dim]\n")

    agent = PDF2MD(
        input_path=input_path,
        output_path=output_path,
        combine_page=args.combine_page,
        trans_num=args.trans_num,
    )

    try:
        if args.pure:
            console.print("[bold]运行模式: 仅 OCR[/bold]\n")
            agent.pure_pdf2md()
        else:
            console.print("[bold]运行模式: OCR + 翻译[/bold]\n")
            await agent.pdf2md()
    except Exception as exc:
        console.print(f"\n[red bold]✗ 处理失败: {exc}[/red bold]")
        return 1

    console.print(f"\n[green bold]✓ 全部完成！结果保存在: {output_path}[/green bold]")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ 用户中断[/yellow]")
        sys.exit(130)
