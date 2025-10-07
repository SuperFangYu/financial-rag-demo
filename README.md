金融智能问答系统（RAG + Agent + API + Java Integration）

本项目基于 \*\*LangChain + FAISS + 智谱AI (ZhipuAI)\*\* 构建，实现了从金融文档中自动抽取知识、进行语义检索、智能问答与计算分析的完整流程。



---



\## 项目结构

project/

├── rag\_basic/ # 简单版 RAG 示例（单文档问答）

│ ├── load\_pdf.py

│ ├── qa.py

│ └── faiss\_index/

│

├── rag\_advanced/ # 高级版 RAG（多文档+多链）

│ ├── multi\_doc.py # 多文档向量化与索引构建

│ ├── sequential\_chain.py # 两条链（摘要链+总结链）

│ ├── agent\_tools.py # 自定义工具：增长率计算

│ ├── tencent\_news.pdf

│ ├── tencent\_financial.pdf

│ └── faiss\_multi/

│

├── api/ # FastAPI 后端接口

│ ├── main.py # 启动文件

│ ├── routers/

│ ├── models.py

│ └── ...

│

├── integration/ # Java SpringBoot 集成模块

│ └── springboot\_client/

│ ├── src/

│ ├── pom.xml

│ └── ...

│

├── requirements.txt

├── .gitignore

├── .env.example

└── README.md



---



\##  功能介绍



| 模块 | 功能说明 |

|------|-----------|

| \*\*rag\_basic\*\* | 最简单的 RAG 示例，演示文档加载、切分与问答流程。 |

| \*\*rag\_advanced\*\* | 核心模块，包含多文档向量化、多链问答、增长率计算 Agent。 |

| \*\*api\*\* | 提供统一的后端接口，通过 FastAPI 暴露 RESTful API。 |

| \*\*integration\*\* | Java 端调用接口示例（SpringBoot 集成），可通过 Swagger 调试。 |


\##  数据说明

本项目示例使用的 PDF 文档仅用于展示 RAG（Retrieval-Augmented Generation）流程
由于原始金融报告和新闻稿涉及版权与隐私，仓库中未上传真实文件，仅保留结构与示例样例：
data/sample.pdf
开发者可自行替换为任意 PDF 文档（例如财报、公告或新闻），
系统会自动完成文档加载、分片、向量化存储（FAISS）及问答检索。
若希望快速测试，可将任意 PDF 文件放入 rag_advanced/pdf/ 或 data/ 文件夹中，
然后重新运行多文档加载模块（rag_advanced/multi_doc.py）。

---



\## 环境配置



\### 安装依赖

pip install -r requirements.txt



设置环境变量

复制 .env.example 文件并重命名为 .env

然后填写你的智谱 API Key

ZHIPUAI\_API\_KEY=xxxxxx



---



\## 模块运行说明

1\. 多文档向量化（rag\_advanced/multi\_doc.py）

该模块会加载两个 PDF 文件（腾讯新闻与财报），自动切分并生成向量存入 FAISS 数据库。

python rag\_advanced/multi\_doc.py



&nbsp;2. 链式问答（rag\_advanced/sequential\_chain.py）

调用两条 Chain：

第一条：生成文档摘要；

第二条：基于摘要进行总结性回答。

python rag\_advanced/sequential\_chain.py



&nbsp;3. 智能计算 Agent（rag\_advanced/agent\_tools.py）

用于执行增长率等计算任务。

python rag\_advanced/agent\_tools.py



\## API 启动与调试

1\. 启动 FastAPI

uvicorn api.main:app --reload

浏览器打开：

http://127.0.0.1:8000/docs

在调试页面中输入：

"company\_name": "腾讯",

"question": "2024年利润是多少？"

即可查看返回结果。



2\. 启动 SpringBoot 集成端

在 IDE（如 IntelliJ IDEA）中运行：

SpringbootClientApplication

打开浏览器访问：

http://localhost:8080/swagger-ui/

输入同样的参数，结果与 FastAPI 一致



---



\## 技术栈

LangChain：文档切分、Prompt 设计、Chain 构建

FAISS：向量数据库，存储金融文档的语义索引

智谱AI (ZhipuAI)：大语言模型调用

FastAPI：Python 后端接口服务

SpringBoot：Java 端集成调用示例

Python 3.10+



---



\## 示例问答

用户输入：

"company\_name": "腾讯",

"question": "2024年利润是多少？"

模型返回：

“根据提供的腾讯财务文档摘要，2024年的利润数据主要来自“核心财务指标”和“利润表关键项目”部分。用户询问“2024年利润”，通常指全年净利润（即期内盈利），这是衡量公司整体盈利能力的核心指标。”



---

展示视频链接：https://www.bilibili.com/video/BV1pWxDzFE6g/?spm_id_from=333.1387.upload.video_card.click&vd_source=20eb8bc0049eccfebc078c832b356721

License

MIT License



作者： 方宇

简介： 本项目用于展示多模态 RAG 系统的实现能力与 API 集成经验，可扩展至金融知识库问答或企业内部文档检索场景。

