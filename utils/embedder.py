# # utils/embedder.py

# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np
# import os
# import pickle

# EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

# class Embedder:
#     def __init__(self):
#         self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

#     def embed_texts(self, texts):
#         return self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

#     def build_faiss_index(self, texts, save_path="index/faiss_index.pkl"):
#         if not os.path.exists("index"):
#             os.makedirs("index")

#         embeddings = self.embed_texts(texts)
#         dim = embeddings.shape[1]
#         index = faiss.IndexFlatL2(dim)
#         index.add(embeddings)

#         data = {
#             "index": index,
#             "texts": texts
#         }

#         with open(save_path, "wb") as f:
#             pickle.dump(data, f)

#         print(f"✅ FAISS index saved at: {save_path}")




# utils/embedder.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    def embed_texts(self, texts):
        return self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    def build_faiss_index(self, texts, save_dir="index"):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        embeddings = self.embed_texts(texts)
        dim = embeddings.shape[1]

        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)

        # ✅ Save index separately
        faiss.write_index(index, os.path.join(save_dir, "faiss.index"))

        # ✅ Save texts + embeddings using pickle
        metadata = {
            "texts": texts,
            "embeddings": embeddings
        }

        with open(os.path.join(save_dir, "metadata.pkl"), "wb") as f:
            pickle.dump(metadata, f)

        print(f"✅ FAISS index and metadata saved in '{save_dir}/'")
