from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def load_and_split(files):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_chunks = []
    for f in files:
        loader = PyPDFLoader(f)
        docs = loader.load()
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)
    return all_chunks

def build_index(chunks, index_path="faiss_multi"):
    embeddings = SentenceTransformerEmbeddings(model_name="BAAI/bge-small-zh")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)
    return vectorstore

if __name__ == "__main__":
    files = ["tencent_financial.pdf", "tencent_news.pdf"]
    chunks = load_and_split(files)
    build_index(chunks)
    print("多文档向量库已构建完成")
