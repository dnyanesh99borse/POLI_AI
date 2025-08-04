# # utils/retriever.py

# from sentence_transformers import SentenceTransformer
# import numpy as np
# import faiss
# import pickle

# class Retriever:
#     def __init__(self, index_path="index/faiss_index.pkl", model_name="BAAI/bge-small-en-v1.5"):
#         self.model = SentenceTransformer(model_name)

#         with open(index_path, "rb") as f:
#             data = pickle.load(f)
#             self.index = data["index"]
#             self.texts = data["texts"]

#     def search(self, query, top_k=5):
#         query_embedding = self.model.encode([query])
#         distances, indices = self.index.search(np.array(query_embedding).astype("float32"), top_k)

#         results = []
#         for idx in indices[0]:
#             results.append(self.texts[idx])
#         return results




# utils/retriever.py

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle
import os  
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, index_dir="index", model_name="BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

        # ✅ Load FAISS index
        self.index = faiss.read_index(os.path.join(index_dir, "faiss.index"))

        # ✅ Load texts + embeddings
        with open(os.path.join(index_dir, "metadata.pkl"), "rb") as f:
            data = pickle.load(f)

        self.texts = data["texts"]
        self.embeddings = data["embeddings"]

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding).astype("float32"), top_k)

        results = [self.texts[idx] for idx in indices[0]]
        selected_embeddings = [self.embeddings[idx] for idx in indices[0]]
        return results, selected_embeddings, query_embedding

    def is_relevant(self, query_embedding, chunk_embeddings, threshold=0.5):
        sims = cosine_similarity(query_embedding, chunk_embeddings)
        max_sim = sims.max()
        return max_sim >= threshold
