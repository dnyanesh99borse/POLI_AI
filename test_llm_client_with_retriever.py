# # test_llm_with_retriever.py

# from utils.retriever import Retriever
# from utils.llm_client import ask_llm

# retriever = Retriever()
# query = "What is the waiting period for pre-existing diseases?"

# top_chunks = retriever.search(query, top_k=3)
# context = "\n\n".join(top_chunks)

# answer = ask_llm(query, context)
# print(f"🧠 Answer:\n{answer}")



# test_llm_client.py

from utils.retriever import Retriever
from utils.llm_client import ask_llm

question = input("❓ Enter your question: ")

retriever = Retriever()
chunks, chunk_embeddings, query_embedding = retriever.search(question, top_k=3)

if not retriever.is_relevant(query_embedding, chunk_embeddings):
    print("🧠 Answer:\nSorry, this question is not covered in the document.")
else:
    context = "\n".join(chunks)
    answer = ask_llm(question, context)
    print("🧠 Answer:\n", answer)

