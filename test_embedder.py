# build_index.py

from utils.chunker import extract_chunks_from_pdf
from utils.embedder import Embedder

pdf_path = "data/Arogya Sanjeevani Policy.pdf"  # replace with your actual PDF

chunks = extract_chunks_from_pdf(pdf_path)
print(f"📄 Extracted {len(chunks)} chunks from document.")

embedder = Embedder()
embedder.build_faiss_index(chunks)

