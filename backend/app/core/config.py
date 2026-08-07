import os
from dotenv import load_dotenv

load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./data/vector_store")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "medical_docs")