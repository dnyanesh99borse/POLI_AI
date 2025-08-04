# # utils/llm_client.py


# import os
# import httpx
# from dotenv import load_dotenv

# load_dotenv()
# TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
# MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"  # ✅ Fully supported model

# HEADERS = {
#     "Authorization": f"Bearer {TOGETHER_API_KEY}",
#     "Content-Type": "application/json"
# }


# def ask_llm(question, context, max_tokens=512):
#     messages = [
#         {"role": "system", "content": "You are an expert assistant that answers questions based on policy documents."},
#         {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
#     ]

#     payload = {
#         "model": MODEL_NAME,
#         "messages": messages,
#         "max_tokens": max_tokens,
#         "temperature": 0.3,
#         "top_p": 0.9
#     }

#     try:
#         response = httpx.post(TOGETHER_API_URL, headers=HEADERS, json=payload, timeout=30)
#         response.raise_for_status()
#         result = response.json()
#         return result["choices"][0]["message"]["content"].strip()
#     except Exception as e:
#         return f"⚠️ LLM error: {e}"






# utils/llm_client.py

import os
import httpx
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # ✅ Free & working

HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

def ask_llm(question, context, max_tokens=512):
    messages = [
        {"role": "system", "content": "You are an expert assistant answering questions using the provided context from a policy document."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
    ]

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "top_p": 0.9
    }

    try:
        response = httpx.post(TOGETHER_API_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ LLM error: {e}"

