# Medical RAG Assistant 

A production-ready Retrieval-Augmented Generation (RAG) assistant designed for answering complex medical queries based on loaded medical research documentation.

Built using **FastAPI**, **Streamlit**, **ChromaDB**, and **Ollama (Llama 3.2)**.

---

## System Architecture

```mermaid
graph LR
    A[Streamlit UI<br/>Frontend] -- HTTP POST --> B[FastAPI Backend<br/>API Layer]
    B -- Vector Search --> C[(ChromaDB<br/>Vector Store)]
    B -- Context + Query --> D[Ollama LLM<br/>Llama 3.2]
    D -- Generated Answer --> B
    B -- JSON Response --> A
```
