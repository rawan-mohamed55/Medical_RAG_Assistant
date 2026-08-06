# Medical RAG Assistant 

A production-ready Retrieval-Augmented Generation (RAG) assistant designed for answering complex medical queries based on loaded medical research documentation.

Built using **FastAPI**, **Streamlit**, **ChromaDB**, and **Ollama (Llama 3.2)**.

---

## 📐 System Architecture

```text
+-------------------+      HTTP      +-------------------+      Local Call     +-------------------+
|                   | -------------> |                   | ------------------> |                   |
| Streamlit UI      |                | FastAPI Backend   |                     | Ollama LLM        |
| (Frontend)        | <------------- | (API Layer)       | <------------------ | (Llama 3.2)       |
+-------------------+    JSON Resp   +-------------------+     Prompt Context  +-------------------+
                                               |
                                               | Vector Search
                                               v
                                     +-------------------+
                                     | ChromaDB          |
                                     | (Vector Store)    |
                                     +-------------------+