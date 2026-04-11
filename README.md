# PDF2MD-ZH - PDF转Markdown翻译工具

一个将PDF文档转换为Markdown格式并翻译英文内容为中文的工具。结合了PaddleOCR的文档结构识别和DeepSeek大模型的智能翻译能力。

## ✨ 功能特性

- **PDF结构解析**：使用PaddleOCR-VL-1.5 API提取PDF文档的文本结构和布局
- **智能翻译**：利用DeepSeek大模型将英文内容翻译为中文，保留专业术语和格式
- **双语输出**：生成包含原文和翻译的Markdown文件，便于对照学习
- **图片保存**：自动下载PDF中的图片并保存到本地
- **进度显示**：实时显示处理进度和状态
- **配置管理**：通过环境变量管理API密钥和配置

## 📁 项目结构

```
pdf2md/
├── src/pdf2md/
│   ├── __init__.py          # 包初始化
│   ├── pdf2md.py           # 主处理类
│   ├── paddle_ocr.py       # PaddleOCR API封装
│   └── deepseek_trans.py   # DeepSeek翻译封装
├── pdf/                    # 输入PDF目录
├── md/                     # 输出Markdown目录
├── run.py                  # 运行脚本
├── pyproject.toml          # 项目配置和依赖
├── .env.example           # 环境变量模板
└── README.md              # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

确保已安装Python 3.14+，推荐使用uv进行依赖管理：

```bash
# 克隆项目
git clone <repository-url>
cd pdf2md

# 创建虚拟环境（可选）
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows

# 安装依赖
uv pip install -e .
```

### 2. 配置API密钥

复制环境变量模板并填入你的API密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
# 输入paddle api token 在 paddle ai studio 获取
PADDLE_API_TOKEN=your_paddleocr_token_here

# 输入deepseek api key 在 deepseek api开放平台获取
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

#### API密钥获取方式：
- **PaddleOCR API Token**：访问 [Paddle AI Studio](https://aistudio.baidu.com/) 创建应用获取
- **DeepSeek API Key**：访问 [DeepSeek开放平台](https://platform.deepseek.com/) 注册获取

### 3. 放置PDF文件

将要处理的PDF文件放入 `pdf/` 目录，默认会处理 `pdf/paper.pdf`：

```bash
cp your_document.pdf pdf/paper.pdf
```

### 4. 运行转换

```bash
python run.py
```

或者直接使用模块：

```python
from pdf2md.pdf2md import PDF2MD

# 指定输入输出路径
input_pdf = "path/to/your.pdf"
output_dir = "path/to/output"

# 创建转换器并运行
converter = PDF2MD(input_pdf, output_dir)
converter.pdf2md()
```

## 🔧 工作流程

### 处理流程详解

1. **PDF上传与解析**
   - 将PDF文件Base64编码
   - 调用PaddleOCR-VL-1.5 API进行文档结构分析
   - 获取文本、图片位置和布局信息

2. **文本提取与分割**
   - 从API响应中提取Markdown格式文本
   - 按文档结构分割为多个部分（如章节、段落）

3. **智能翻译**
   - 使用DeepSeek-chat模型进行英文到中文翻译
   - 特殊处理：保留术语、人名、表格内容和引用格式
   - 翻译格式：每段翻译前添加 `> ` 前缀

4. **文件生成**
   - 创建Markdown文件，包含原文和翻译
   - 原文和翻译用空行分隔，便于对照
   - 保存路径：`{output_dir}/doc_{index}.md`

5. **图片下载**
   - 下载文档中的图片
   - 保存到 `{output_dir}/imgs/` 目录
   - 布局图片保存到 `{output_dir}/layout/` 目录

### 输出格式示例

生成的Markdown文件格式：

```markdown
# 原文内容

This is an example paragraph with **bold text** and *italic text*.

Here is a formula: $E = mc^2$

And a block formula:
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

> 这是示例段落的翻译，包含**粗体文本**和*斜体文本*。
>
> 这是一个公式：$E = mc^2$
>
> 以及一个块公式：
> $$
> \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
> $$
```

## ⚙️ 配置说明

### 环境变量

| 变量名 | 说明 | 必需 | 默认值 |
|--------|------|------|--------|
| `PADDLE_API_TOKEN` | PaddleOCR API访问令牌 | 是 | 无 |
| `DEEPSEEK_API_KEY` | DeepSeek API密钥 | 是 | 无 |

### 代码配置

在 `deepseek_trans.py` 中可以调整翻译参数：

```python
self.system_prompt = (
    "将下面 Markdown 文本中的英文自然语言翻译成中文（不翻译术语、人名、引用格式）。"
    "翻译后逻辑严密，语言通顺，行行流畅，符合中文语序"
    "输出格式：每段翻译前加 `> `（表格内元素不需要加 > ），保持原有换行和 Markdown 结构。只输出翻译结果，不要原文。"
)

# 温度参数控制创造性
temperature = 1.3
```

## 📊 当前限制与问题

### 已知问题

1. **分页翻译语义分割问题**
   - PDF分页可能导致语义不连贯
   - 跨页的段落可能被错误分割
   - 解决方案：需要实现智能段落合并算法

2. **PaddleOCR API限制**
   - 单次处理最多100页PDF
   - 大文件需要分割处理
   - API响应时间受文件大小影响

3. **DeepSeek串行翻译**
   - 当前为串行翻译，处理速度慢
   - 长文档翻译耗时较长
   - 缺乏并发控制和速率限制

4. **公式格式问题**
   - 行内公式空格问题：`$ 内容 $` 格式不正确
   - 块公式缩进问题：`$$` 公式 `$$` 有缩进导致无法渲染
   - 需要正则表达式修复公式格式

### 性能限制

| 项目 | 限制 | 影响 |
|------|------|------|
| PDF大小 | 受PaddleOCR API限制 | 大文件需要分割 |
| 页数 | ≤100页/次 | 超限需要分批次 |
| 翻译速度 | 串行处理 | 长文档耗时 |
| 网络依赖 | 需要稳定网络 | API调用可能失败 |

## 🚧 后续改进计划

### 短期改进（v0.2.0）

1. **多页PDF处理**
   - 实现PDF自动分割功能
   - 支持100页以上文档处理
   - 分批次调用PaddleOCR API

2. **异步翻译优化**
   - 使用asyncio实现并发翻译
   - 控制API调用频率和并发数
   - 添加重试机制和错误处理

3. **公式格式修复**
   - 正则表达式修复行内公式空格
   - 移除块公式的缩进问题
   - 确保公式在Markdown中正确渲染



## 🛠️ 技术栈

- **Python 3.14+**：主要编程语言
- **PaddleOCR-VL-1.5**：文档结构识别API
- **DeepSeek-chat**：大语言模型翻译
- **requests**：HTTP客户端库
- **python-dotenv**：环境变量管理
- **openai**：DeepSeek API客户端

## 📝 使用示例

### 基本使用

```python
from pdf2md.pdf2md import PDF2MD

# 初始化转换器
converter = PDF2MD(
    input_path="documents/report.pdf",
    output_path="output/translated"
)

# 执行转换
converter.pdf2md()
```

### 自定义输出

```python
# 可以修改deepseek_trans.py中的系统提示词
# 调整翻译风格和格式要求

system_prompt = """
你是一个专业的学术文档翻译助手。
请将以下英文Markdown内容翻译为中文，要求：
1. 保留所有专业术语和公式
2. 保持原文的Markdown格式
3. 翻译流畅自然，符合学术规范
4. 每段翻译前添加'> '前缀
"""
```

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request



## 🙏 致谢

- [PaddlePaddle](https://www.paddlepaddle.org.cn/) 提供优秀的OCR技术
- [DeepSeek](https://www.deepseek.com/) 提供强大的语言模型
- 所有贡献者和用户的支持



---

**注意**：本项目依赖第三方API服务，请遵守相关服务的使用条款和限制。处理敏感文档时请注意数据安全。
