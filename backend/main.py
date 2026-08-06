from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions
import ollama

app = FastAPI(title="Medical RAG Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMBED_MODEL = "all-MiniLM-L6-v2"
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
chroma_client = chromadb.PersistentClient(path="D:/medical_rag/chroma_db")
collection = chroma_client.get_or_create_collection(name="medical_docs", embedding_function=embedding_func)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Medical RAG API is operational"}

@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    if not req.question.strip():
        raise HTTPException(status_code=422, detail="Question cannot be empty")
        
    results = collection.query(query_texts=[req.question], n_results=3)
    docs = results['documents'][0] if results['documents'] else []
    context = "\n".join(docs)
    
    prompt = f"Use the medical context below to answer accurately and concisely.\nContext:\n{context}\n\nQuestion: {req.question}\nAnswer:"
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': prompt}])
    
    return QueryResponse(answer=response['message']['content'], sources=docs)