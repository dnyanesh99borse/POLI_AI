# test_retriever.py

from utils.retriever import Retriever

retriever = Retriever()
query = "What is the waiting period for pre-existing diseases?"
results = retriever.search(query, top_k=3)

print("🔍 Top Matches:")
for i, chunk in enumerate(results, 1):
    print(f"{i}. {chunk[:200]}...\n")  # print first 200 chars only
