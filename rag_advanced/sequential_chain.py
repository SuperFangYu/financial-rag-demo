from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatZhipuAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 读取 API Key
api_key = os.getenv("ZHIPUAI_API_KEY")

def retrieve_docs(query, index_path="faiss_multi"):
    embeddings = SentenceTransformerEmbeddings(model_name="BAAI/bge-small-zh")
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    return retriever.get_relevant_documents(query)

def build_chain():
    llm = ChatZhipuAI(model="glm-4.5", temperature=0, api_key=api_key)
    # Step1: 检索到的内容 → 文本
    template1 = "根据以下文档内容，提取关键信息：\n{docs}"
    prompt1 = PromptTemplate(input_variables=["docs"], template=template1)
    chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="summary")

    # Step2: 基于 summary + 用户问题，生成最终回答
    template2 = "用户问题：{question}\n文档摘要：{summary}\n请生成最终回答。"
    prompt2 = PromptTemplate(input_variables=["question", "summary"], template=template2)
    chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="final_answer")

    return SequentialChain(
        chains=[chain1, chain2],
        input_variables=["docs", "question"],
        output_variables=["summary", "final_answer"],
        verbose=True
    )

if __name__ == "__main__":
    query = "腾讯 2024 年净利润 + 最近新闻摘要"
    docs = retrieve_docs(query)
    chain = build_chain()
    result = chain.invoke({"docs": str(docs), "question": query})
    print("最终回答：", result["final_answer"])
