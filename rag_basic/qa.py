from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatZhipuAI
from langchain.chains import RetrievalQA
from langchain_community.embeddings import SentenceTransformerEmbeddings
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 读取 API Key
api_key = os.getenv("ZHIPUAI_API_KEY")

def run_qa(query, index_path="faiss_index"):
    # 初始化 ZhipuAI 的 Chat 实例
    chat = ChatZhipuAI(model="glm-4.5", temperature=0, api_key=api_key)

    # 加载 FAISS 向量数据库
    embeddings = SentenceTransformerEmbeddings(model_name="BAAI/bge-small-zh")
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    # 使用 RetrievalQA 构建链式问答
    qa_chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff"
    )

    result = qa_chain.invoke(query)
    return result

if __name__ == "__main__":
    question = "净利润是多少？"
    answer = run_qa(question)
    print("问题：", question)
    print("回答：", answer)
