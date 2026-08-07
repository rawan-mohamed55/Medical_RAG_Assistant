import chromadb
from chromadb.utils import embedding_functions
from app.core.config import EMBED_MODEL, VECTOR_STORE_PATH, COLLECTION_NAME

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
chroma_client = chromadb.PersistentClient(path=VECTOR_STORE_PATH)
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

def retrieve_context(question: str, n_results: int = 3):
    results = collection.query(query_texts=[question], n_results=n_results)
    docs = results['documents'][0] if results['documents'] else []
    return docs