# 书籍自动生成器

## 项目介绍
这是一个利用OpenAI的GPT模型自动生成书籍大纲和内容的工具。您可以通过简单的命令行参数，指定要生成的书名，然后系统会为您生成相应的大纲或者内容。

## 安装依赖
首先，确保您已经安装了Python环境。然后，您需要安装必要的Python库。在项目根目录下，运行：

```bash
pip install openai
```

## 如何使用
0. **初始化配置文件**:
   将template.config.json 修改为config.json 
   填写你的openai密钥
   [可选] 将官方地址修改为你的openai代理地址（暂未加入proxy功能，目前仅支持代理地址）
1. **生成大纲**:
   要生成书籍的大纲，您可以使用以下命令：

   ```bash
   python main.py [书名] --generate outline
   ```

   例如，要为“机器学习”这本书生成大纲，您可以运行：

   ```bash
   python main.py 机器学习 --generate outline
   ```
   而后您可以在生成/[书名]/book_outline.md中找到并编辑该大纲

2. **生成章节内容**:
   要生成特定章节的内容，您可以使用以下命令：

   ```bash
   python main.py [书名] --generate content --start_chapter [起始章节] --end_chapter [结束章节]
   ```

   例如，要生成“机器学习”这本书的第1章到第2章的内容，您可以运行：

   ```bash
   python main.py 机器学习 --generate content --start_chapter 1 --end_chapter 2
   ```

## 注意事项
- 请确保您已经设置了正确的OpenAI API密钥和基础URL。
- 生成的内容取决于OpenAI模型的训练数据，可能需要进一步的编辑和修订。

