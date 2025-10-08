from fastapi import APIRouter
from api.models import AskRequest, AskResponse
from rag_advanced.sequential_chain import retrieve_docs
from rag_advanced.sequential_chain import build_chain

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    query = request.question
    docs = retrieve_docs(query, "rag_advanced/faiss_multi")
    chain = build_chain()
    result = chain.invoke({"docs": str(docs), "question": query})

    return AskResponse(answer=result["final_answer"])
