import ollama
from app.core.config import OLLAMA_MODEL

def generate_answer(question: str, docs: list[str]) -> str:
    context = "\n".join(docs)
    prompt = f"Use the medical context below to answer accurately and concisely.\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = ollama.chat(model=OLLAMA_MODEL, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']