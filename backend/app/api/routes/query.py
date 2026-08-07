from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest, QueryResponse
from app.services.retrieval import retrieve_context
from app.services.generation import generate_answer

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Medical RAG API is operational"}

@router.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    if not req.question.strip():
        raise HTTPException(status_code=422, detail="Question cannot be empty")

    docs = retrieve_context(req.question)
    answer = generate_answer(req.question, docs)

    return QueryResponse(answer=answer, sources=docs)