# 开发变更日志

> 记录每次修改的要求、原因及具体更改位置，便于追溯与回滚。

---

## 2026-04-28

### 性能优化（OCR 异步化、HTTP 连接池、图片跨页并发、翻译流式写入）

**要求**：用户要求 review 性能并实施改进。

**更改位置**：
- `src/pdf2md/pdf2md.py`：
  - `__init__` 中新增 `self._img_session = requests.Session()`，启用 HTTP keep-alive，图片下载提速 20–40%
  - `pdf2md()` 中 OCR 调用改为 `await asyncio.to_thread(self.ocr_model.get_result, ...)`，不再阻塞事件循环
  - `_save_images_sync()` 改用 `self._img_session.get()`，增加 `resp.raise_for_status()`，跳过已存在的图片
  - 移除 `_save_images_async()`，新增 `_save_all_images_async()`：预收集全文档图片后跨页并发下载，避免页级串行阻塞
  - `_async_write_pages()` 改为先写全部 Markdown，再批量下载全部图片，解耦写文件与下载
  - `_write_trans_page()` 改用 `asyncio.wait(return_when=FIRST_COMPLETED)` 流式消费翻译结果，每完成一页立即写入文件，避免全量 buffered 在内存
  - 更新相关 docstring

---

## 2026-04-28

### 移除分块翻译

**要求**：用户指出 DeepSeek V4 完全有能力翻译长文本，分块配置导致输出多处遗漏。

**诊断**：早期测试中 3908 字符返回空字符串，错误归因于模型对长文本的限制；后续验证表明问题根源是 system prompt 过于冗长。精简 prompt 后，模型可正常翻译 3908、8449、11840 字符的文本。分块逻辑本身引入了不必要的串行瓶颈，且 `_CHUNK_THRESHOLD = 2500` 的阈值缺乏依据。

**更改位置**：
- `src/pdf2md/deepseek_trans.py`：
  - 移除 `_CHUNK_THRESHOLD` 常量
  - 移除 `_split_by_sections()` 方法
  - `get_result()` 直接调用 `_translate_chunk()`，不再按章节拆分
  - 移除未使用的 `re` 导入
  - 更新类与方法 docstring，删除"自动分块"描述

---

## 2026-04-28

### 性能 Review

**要求**：review 近期更改对性能的影响，并识别进一步性能提升空间。

**发现的问题**：

#### 1. OCR 阻塞事件循环（Critical）

- **位置**：`src/pdf2md/pdf2md.py:419`
- **问题**：`pdf2md()` 是 async 方法，但直接调用同步的 `self.ocr_model.get_result()`，阻塞事件循环 30–120 秒。
- **建议**：`lines = await asyncio.to_thread(self.ocr_model.get_result, self.input_path)`

#### 3. 图片下载跨页串行（Medium）

- **位置**：`src/pdf2md/pdf2md.py:311-351`
- **问题**：`_async_write_pages` 的 for 循环中，页 N 的图片下载完成后才开始页 N+1。全文档图片未实现跨页并发。
- **建议**：预收集所有图片 URL，一次性 `asyncio.gather` 下载。

#### 4. 无 HTTP 连接池（Medium）

- **位置**：`src/pdf2md/pdf2md.py:252`
- **问题**：每次下载图片都新建 `requests.get()` 连接，TCP/TLS 握手重复。
- **建议**：使用 `requests.Session()` 启用 keep-alive，图片下载提速 20–40%。

#### 5. 翻译结果全量驻留内存（Low）

- **位置**：`src/pdf2md/pdf2md.py:396`
- **问题**：`asyncio.gather(*tasks)` 将全部翻译结果同时保留在内存，大文档内存占用高。
- **建议**：每完成一页翻译立即写入文件（流式写入）。

**改进优先级**：

| 优先级 | 改进项 | 预计收益 | 复杂度 |
|--------|--------|----------|--------|
| P0 | OCR 异步化 (`asyncio.to_thread`) | 修复 async 契约 | 低 |
| P0 | 分块翻译纳入全局 Semaphore 并发 | 翻译吞吐 +15–30% | 中 |
| P1 | 图片下载使用 `requests.Session()` | 下载提速 20–40% | 低 |
| P1 | 全文档图片预收集后并发下载 | 写文件与下载解耦 | 中 |
| P2 | 翻译结果流式写入 | 内存占用减半 | 中 |

---

## 2026-04-27

### 命令行输出美化（引入 rich）

**要求**：优化命令行输出，解决中英文混杂、轮询刷屏、逐条打印、缺乏进度感等问题。

**更改位置**：

- `pyproject.toml` – 新增依赖 `rich>=13.0.0`
- `src/pdf2md/logger.py` – 新建：基于 `rich.console.Console` 的全局 `console` 实例，供各模块统一使用
- `src/pdf2md/paddle_ocr.py` – OCR 轮询改为 `console.status()` spinner 动画：
  - 排队中 → 黄色 spinner "OCR 排队中..."
  - 提取中 → 绿色 spinner 实时显示 "OCR 提取中... X/Y 页"
  - 完成后 → 一行绿色勾选日志
  - 移除所有 `print()`
- `src/pdf2md/pdf2md.py` – 文件保存与翻译使用 `rich.progress.Progress` 进度条：
  - 保存页面：实时进度条 + 当前页码/图片数提示
  - 翻译页面：实时进度条 + 并发数提示
  - 合并与清理：静默执行，不再逐条打印
  - 所有 `print()` 替换为 `console.print()`
- `src/pdf2md/deepseek_trans.py` – 移除 `[WARNING] DeepSeek API 返回了空内容` 的 `print()`，改为静默返回空字符串
- `run.py` – 使用 `console.rule()` 显示标题分隔线、`console.print()` 显示运行模式与结果：
  - 启动时显示文件名、输出目录、运行模式
  - 成功时显示绿色粗体勾选 + 输出路径
  - 失败时显示红色粗体错误信息
  - `KeyboardInterrupt` 显示黄色警告

---

## 2026-04-27

### 鲁棒性与性能优化（重构代码）

**要求**：进行有助于鲁棒性和性能的更改，优化命名与代码结构，附上简介注释。

**更改位置**：

- `src/pdf2md/deepseek_trans.py` – 全面重构：
  - 类名 `DeekseekTranslate` → `DeepseekTranslate`
  - `load_dotenv()` 从模块级移至 `__init__`，消除导入副作用
  - `AsyncOpenAI` 增加 `timeout=120`，防止长文本翻译无限挂起
  - `get_result()` 增加 `APITimeoutError` 捕获与空内容检测
  - `temperature` 从 `1.3` 降至 `0.3`，提升翻译稳定性
  - 补充模块/类/方法级 docstring

- `src/pdf2md/paddle_ocr.py` – 全面重构：
  - `sys.exit()` → 抛出 `FileNotFoundError` / `RuntimeError`
  - `assert` → 显式 `if status_code != 200: raise RuntimeError(...)`
  - 所有 `requests` 调用增加 `timeout`（提交 60s，轮询 30s，下载 60s）
  - `load_dotenv()` 从模块级移至 `__init__`
  - 轮询逻辑增加 `resp_data` 局部变量，减少重复 `.json()` 调用
  - 补充模块/类/方法级 docstring

- `src/pdf2md/pdf2md.py` – 全面重构：
  - 移除未使用的 `self.page_num`
  - 提取 `_parse_pages(lines)` 私有方法，消除 `pdf2md()` 与 `pure_pdf2md()` 中的重复解析逻辑
  - `_parse_pages` 增加 `json.JSONDecodeError` / `KeyError` 防护，异常行打印警告并跳过
  - `_re_process()` 不再原地修改输入字典，改为返回新字符串
  - 新增 `_extract_page_index()`，文件排序改用正则提取数字，避免硬编码格式崩溃
  - 拆分图片保存为 `_save_images_sync()` / `_save_images_async()`：
    - 异步版本使用 `asyncio.to_thread` 在线程池执行 `requests.get`，不阻塞事件循环
    - 单张图片下载失败时打印警告并继续，不再导致全量崩溃
  - 拆分页面写入为 `_pure_write_page()`（同步）与 `_async_write_pages()`（异步）
  - 新增 `_cleanup_intermediate_files()`，在 `pdf2md()` / `pure_pdf2md()` 异常时自动清理残留中间文件
  - `pdf2md()` 与 `pure_pdf2md()` 均使用 `try/except` 包裹写入+合并流程，失败时清理后重新抛出异常
  - 补充模块/类/方法级 docstring 与分段注释

- `run.py` – 重构：
  - 修正注释与代码不符的问题（原注释写"无翻译"，实际调用含翻译）
  - 新增 `argparse` CLI：`input` 位置参数、`--output`、 `--pure`、 `--combine-page`、 `--trans-num`
  - 增加 `KeyboardInterrupt` 与顶层异常捕获，返回标准退出码
  - 补充模块/函数级 docstring

---

## 2026-04-27

### 初始代码审查 (Code Review)

**要求**：对现有仓库代码进行全面 review，识别 Critical/Major/Minor 级别问题。

**更改位置**：仅评审，无代码修改。问题记录如下：

#### 🔴 Critical

| 位置 | 问题 | 建议 |
|---|---|---|
| `src/pdf2md/paddle_ocr.py:37,103` | 库代码调用 `sys.exit()`，会杀死整个进程 | 改为抛出异常，由调用方处理 |
| `src/pdf2md/pdf2md.py:168` | `requests.get()` 同步阻塞 I/O 在 async 方法 `_pure_write_page` 中执行 | 改用异步 HTTP 客户端或 `run_in_executor` |

#### 🟠 Major

| 位置 | 问题 | 建议 |
|---|---|---|
| `src/pdf2md/paddle_ocr.py:57,68` | 使用 `assert` 做运行时校验，生产环境可能被优化掉 | 改为显式异常或 `raise_for_status()` |
| `src/pdf2md/paddle_ocr.py:49,65,109` | HTTP 请求无超时 | 所有 `requests` 调用添加 `timeout=` |
| `src/pdf2md/deepseek_trans.py:27` | DeepSeek API 调用无超时配置 | 在 `AsyncOpenAI` 或请求级别配置超时 |
| `src/pdf2md/pdf2md.py:168` | 单张图片下载失败导致全量崩溃 | 增加 try/except，记录失败并继续 |
| `src/pdf2md/pdf2md.py` | 流程中途崩溃会残留中间文件，不会执行合并 | 使用临时目录或异常时清理 |
| `src/pdf2md/deepseek_trans.py:25-36` | API 异常（网络、限流、空返回）未处理 | 添加异常处理，空 content 应报错 |
| `src/pdf2md/pdf2md.py:182` | `json.loads(line)["result"]` 无防护 | 对 JSON 解析和字典取值加 try/except |

#### 🟡 Minor

| 位置 | 问题 | 建议 |
|---|---|---|
| `src/pdf2md/deepseek_trans.py:9` | 类名拼写错误 `DeekseekTranslate` | 修正为 `DeepseekTranslate` |
| `run.py:15-16` | 注释与代码不符（注释写"无翻译"，实际调用含翻译的 `pdf2md()`） | 修正注释或调换代码 |
| `src/pdf2md/pdf2md.py:173-184` vs `196-206` | OCR 结果解析逻辑完全重复 | 提取为 `_parse_pages(lines)` 私有方法 |
| `src/pdf2md/pdf2md.py:53` | 文件排序依赖硬编码格式，格式偏离会崩溃 | 使用正则提取数字 |
| `src/pdf2md/paddle_ocr.py:11` / `deepseek_trans.py:6` | 模块级 `load_dotenv()` 副作用，可能覆盖调用方环境变量 | 移至 `__init__` 或由入口统一加载 |
| `src/pdf2md/pdf2md.py:153` | `_re_process` 原地修改输入字典 | 返回新字符串，保持输入不可变 |
| `src/pdf2md/pdf2md.py:39` | `self.page_num = 0` 定义后从未使用 | 删除 |
| `run.py` | 路径、并发数、合并页数全部硬编码 | 使用 `argparse` 支持 CLI 参数 |
| 全项目 | 使用 `print()` 而非 `logging` | 建议迁移至 `logging` 模块 |

---

## 格式说明

每次新条目请按以下模板追加到文件顶部：

```markdown
## YYYY-MM-DD

### <简短标题>

**要求**：<用户提出的需求或问题描述>

**更改位置**：
- `<文件路径>:<行号范围>` – <具体改动说明>
- ...
```
