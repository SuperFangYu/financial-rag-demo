from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def build_faiss_index(chunks, index_path="faiss_index"):
    embeddings = SentenceTransformerEmbeddings(model_name="BAAI/bge-small-zh")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore

if __name__ == "__main__":
    from load_pdf import load_and_split
    chunks = load_and_split("company_financial_statements.pdf")
    build_faiss_index(chunks)
    print("FAISS 索引已保存！")
