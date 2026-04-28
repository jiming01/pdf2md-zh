# AGENTS.md

## Project Overview

`pdf2md` is a Python CLI tool that converts PDFs to Markdown using the PaddleOCR-VL-1.5 API, with optional Chinese translation via DeepSeek. It is a single-package project with no test suite, CI, or linting configuration.

## Environment & Dependencies

- **Python**: `>=3.14` (enforced by `.python-version` and `pyproject.toml`).
- **Package manager**: `uv`. Use `uv sync` to install dependencies and create the venv.
- **Required env vars** (create `.env` from `.env.example`):
  - `PADDLE_API_TOKEN` – from Baidu AI Studio.
  - `DEEPSEEK_API_KEY` – from DeepSeek platform.

> Do not commit `.env`; it is gitignored.

## Running the Tool

Entry point is `run.py` (async). Supports CLI arguments:

```bash
python run.py <input.pdf> [--output OUTPUT_DIR] [--pure] [--combine-page N] [--trans-num N]
```

- `--pure` skips translation (OCR only).
- Defaults: `--combine-page 50`, `--trans-num 10`.

Example:
```bash
python run.py ./pdf/paper.pdf --output ./md/paper --trans-num 20
```

## Architecture

```
src/pdf2md/
├── pdf2md.py          # PDF2MD orchestrator: OCR → (translate) → combine pages
├── paddle_ocr.py      # PaddleOCR API client (blocking HTTP polling)
└── deepseek_trans.py  # DeepSeek async translation client
```

### Execution Modes

`PDF2MD` in `src/pdf2md/pdf2md.py` exposes two methods:

- `pure_pdf2md()` – OCR only, no translation.
- `pdf2md()` – OCR + async translation.

Both modes write per-page files to `output_path`, then combine them into grouped Markdown files and a `_full` variant.

### Output Files

For a PDF named `paper.pdf` with default `combine_page=50`:

```
md/paper/
├── group_0.md          # pages 0–49 (original OCR)
├── group_trans_0.md    # pages 0–49 (translated)
├── group_full.md       # all pages merged (original)
├── group_trans_full.md # all pages merged (translated)
└── images/             # downloaded images referenced by both MD files
```

Original per-page files (`doc_{i}.md`, `doc_{i}_trans.md`) are deleted after combining.

### Concurrency

Translation uses `asyncio.Semaphore(self.trans_num)` (default 10) to limit parallel DeepSeek API calls. The OCR step itself is blocking (synchronous HTTP polling to PaddleOCR) but runs in a separate thread via `asyncio.to_thread` so it does not block the event loop.

## Key Code Behaviors

- **Style injection**: Combined Markdown files prepend a hardcoded CSS `<style>` block (the `STYLE` constant in `pdf2md.py`).
- **Formula cleanup**: `_re_process()` strips spaces around inline `$...$` and normalizes block `$$...$$` with newlines.
- **Image deduplication**: Images are downloaded once into `output_path` and referenced by both original and translated Markdown files.
- **Exit on OCR failure**: `paddle_ocr.py` raises `FileNotFoundError` (missing PDF) or `RuntimeError` (Paddle job failure) instead of calling `sys.exit(1)`.

## What Not to Expect

- No tests, no type-checker, no linter, and no CI workflows.
- No package publishing scripts.
- `src/pdf2md/__init__.py` is a stub (`hello()`); real API is imported directly from submodule files.
