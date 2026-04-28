# pdf2md-zh

一个实用的 PDF 转 Markdown 工具。项目基于 PaddleOCR 提取文档结构与排版，并调用 DeepSeek 大模型对提取的内容进行翻译，最终支持分离输出原始 OCR 的 Markdown 文件和纯翻译的 Markdown 文件。

## 主要特性

- **分离式双重输出**：支持仅进行 OCR 提取，或同时进行 OCR 提取与全量翻译，且原生排版文件（OCR 结果）与翻译文件分离输出。
- **图片共享复用**：解析 Markdown 结果并自动下载保存原文档中的配图，原始文档与翻译文档智能复用同一份图片文件，节省空间。
- **文档结构解析**：通过 PaddleOCR-VL-1.5 接口提取 PDF 的文本、图片及布局。
- **并发智能翻译**：基于 `asyncio` 和 DeepSeek API 实现多页并发翻译，显著提升长文档处理速度。
- **排版清理与优化**：自动修复 LaTeX 行内及块级公式的空格和缩进问题，确保在 Markdown 中正常渲染。
- **自动分页聚合**：将原始结果和翻译结果分别按指定页数自动合并（如每 50 页合成一个文件），方便阅读与管理。
- **异常自动清理**：处理流程中途失败时自动清理残留中间文件，避免目录混乱。
- **网络超时保护**：所有 API 请求均配置超时，防止无限挂起。

## 项目结构

```text
.
├── md/                     # 输出目录（Markdown 文件与图片存放处）
├── pdf/                    # 输入目录（待处理的 PDF 文件存放处）
├── src/pdf2md/             # 核心逻辑源码
│   ├── deepseek_trans.py   # DeepSeek 异步翻译客户端
│   ├── paddle_ocr.py       # PaddleOCR API 同步轮询客户端
│   └── pdf2md.py           # 核心编排：OCR → 翻译 → 合并
├── .env.example            # 环境变量配置模板
├── pyproject.toml          # 项目配置与依赖说明
├── run.py                  # CLI 入口脚本
└── log.md                  # 开发变更日志
```

## 环境准备

本项目推荐使用 [uv](https://github.com/astral-sh/uv) 进行环境和依赖管理。

1. **安装依赖**
   ```bash
   uv sync
   # 或者使用
   uv pip install -e .
   ```

2. **配置环境变量**
   复制 `.env.example` 文件为 `.env`：
   ```bash
   cp .env.example .env
   ```
   在 `.env` 中填入你的 API 密钥：
   ```env
   PADDLE_API_TOKEN=your_paddleocr_token_here
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```
   > API 密钥获取：
   > - Paddle API Token: [百度飞桨 AI Studio](https://aistudio.baidu.com/)
   > - DeepSeek API Key: [DeepSeek 开放平台](https://platform.deepseek.com/)

## 使用说明

`run.py` 提供命令行接口，无需修改源码即可调整运行参数。

### 快速开始

```bash
# 默认模式：OCR + 翻译（使用默认路径 ./pdf/DeepSeek_V4.pdf）
python run.py

# 指定 PDF 文件
python run.py ./pdf/paper.pdf

# 指定输出目录
python run.py ./pdf/paper.pdf -o ./output/my_paper
```

### 运行模式

```bash
# 模式 1：仅 OCR，不调用翻译
python run.py ./pdf/paper.pdf --pure

# 模式 2：OCR + 翻译（默认）
python run.py ./pdf/paper.pdf
```

### 高级参数

```bash
python run.py ./pdf/paper.pdf \
    -o ./md/paper \
    --combine-page 50 \      # 每组合并页数（默认 50）
    --trans-num 10            # 翻译最大并发数（默认 10）
```

完整参数列表：

```bash
$ python run.py --help
usage: run.py [-h] [-o OUTPUT] [--pure] [--combine-page COMBINE_PAGE] [--trans-num TRANS_NUM] [input]

positional arguments:
  input                 输入 PDF 文件路径 (默认: ./pdf/DeepSeek_V4.pdf)

options:
  -h, --help            显示帮助信息
  -o, --output OUTPUT   输出目录路径 (默认: ./md/<pdf文件名>)
  --pure                仅 OCR，不进行翻译
  --combine-page COMBINE_PAGE  每组合并页数 (默认: 50)
  --trans-num TRANS_NUM  翻译最大并发数 (默认: 10)
```

### 输出文件

处理完成后，生成的文本与图片统一保存在 `md/<pdf-文件名>/` 目录下：

```
md/paper/
├── group_0.md          # 第 0~49 页（原始 OCR）
├── group_trans_0.md    # 第 0~49 页（翻译）
├── group_full.md       # 全部页面合并（原始 OCR）
├── group_trans_full.md # 全部页面合并（翻译）
└── images/             # 下载的配图（原始与翻译文件共享引用）
```

## 注意事项

- OCR 识别效果和最终翻译格式直接依赖于底层模型（PaddleOCR 与 DeepSeek）的能力。实际使用中可能出现排版错位、公式识别不准或特殊字符遗漏等情况。
- 图片下载失败不会中断整体流程，工具会打印警告并继续处理。
- 若处理过程中途崩溃，工具会自动清理已生成的中间文件，避免目录残留。
- 翻译并发数（`--trans-num`）请根据 DeepSeek API 的速率限制适当调整，避免触发限流。

## 效果展示

由于 GitHub 的 Markdown 渲染对于公式不友好，下面展示本工具生成的双语翻译文本在 Obsidian 等专业 Markdown 软件中的实际渲染效果：

<div align="center">
  <img src="example/capture_20260411171432028.bmp" width="75%" />
  <img src="example/capture_20260411171646539.bmp" width="75%" />
  <img src="example/capture_20260411171732813.bmp" width="75%" />
</div>
