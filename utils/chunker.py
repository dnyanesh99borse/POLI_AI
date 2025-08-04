# # utils/chunker.py

# import fitz  # PyMuPDF

# def extract_chunks_from_pdf(pdf_path, chunk_size=300):
#     doc = fitz.open(pdf_path)
#     text = ""

#     for page in doc:
#         text += page.get_text()

#     # Split into sentences or chunks of approx size
#     words = text.split()
#     chunks = []
#     current_chunk = []

#     for word in words:
#         current_chunk.append(word)
#         if len(current_chunk) >= chunk_size:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = []

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks






# utils/chunker.py

import fitz  # PyMuPDF
import re

class Chunker:
    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def chunk_pdf(self, file_path):
        doc = fitz.open(file_path)
        full_text = ""

        for page in doc:
            full_text += page.get_text()

        full_text = self.clean_text(full_text)
        return self.chunk_text(full_text)

    def chunk_text(self, text):
        words = text.split()
        chunks = []

        for i in range(0, len(words), self.chunk_size):
            chunk = " ".join(words[i:i + self.chunk_size])
            chunks.append(chunk)

        return chunks
