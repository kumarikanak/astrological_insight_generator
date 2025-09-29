import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        embeddings = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return embeddings

class VectorRetriever:
    def __init__(self, embeddings, docs):
        self.embeddings = embeddings.astype('float32')
        self.docs = docs
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve(self, query_embedding, top_k=3):
        query_embedding = np.array(query_embedding).astype('float32').reshape(1, -1)
        D, I = self.index.search(query_embedding, top_k)
        return [self.docs[i] for i in I[0]]
