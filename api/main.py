from fastapi import FastAPI
from api.routers import ask

app = FastAPI(title="RAG QA API", version="0.1")

# 挂载路由
app.include_router(ask.router, prefix="/api", tags=["Q&A"])
