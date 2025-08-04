# generate_index.py

from utils.embedder import Embedder
from utils.chunker import Chunker

# 🧾 Replace with your real PDF file path
PDF_PATH = "data/Arogya_Sanjeevani_Policy.pdf" 

chunker = Chunker()
chunks = chunker.chunk_pdf(PDF_PATH)

embedder = Embedder()
embedder.build_faiss_index(chunks)

print("✅ Index regenerated successfully.")
