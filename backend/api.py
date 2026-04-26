# backend/api.py

from fastapi import FastAPI
from pydantic import BaseModel

# apna RAG pipeline import
from rag_pipeline import create_rag_pipeline

app = FastAPI()

# 🔥 RAG load once (important for performance)
rag = create_rag_pipeline()


# Request body structure
class QueryRequest(BaseModel):
    question: str


# API endpoint
@app.post("/chat")
def chat(request: QueryRequest):
    answer = rag(request.question)
    return {"answer": answer}