from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    chunks = load_and_split("company_financial_statements.pdf")
    print(f"切分后的文本块数量：{len(chunks)}")
    print(chunks[0])
