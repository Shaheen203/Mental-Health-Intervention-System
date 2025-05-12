from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
import re

with open("eda_summary.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

split_texts = [line.strip() for line in raw_text.strip().splitlines() if line.strip()]

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_texts(split_texts, embedding_model)

import difflib

def ask_question(query: str) -> str:
    results = db.similarity_search_with_score(query, k=5)

    if not results:
        return (
            "I couldn't find anything relevant in the EDA summary.\n\n"
            "Still, if you're feeling overwhelmed, try some deep breathing, take a walk, or talk to someone you trust. "
        )

    seen = set()
    response_chunks = []

    for doc, score in results:
        paragraph = doc.page_content.strip()

        # Avoid duplicate content using fuzzy match
        is_similar = any(
            difflib.SequenceMatcher(None, paragraph.lower(), prev.lower()).ratio() > 0.85
            for prev in seen
        )

        if not is_similar and len(paragraph.split()) > 5:
            seen.add(paragraph)
            response_chunks.append(f"• {paragraph}")

        if len(response_chunks) == 2:
            break

    if not response_chunks:
        return (
            "I couldn't find anything very relevant. But you're not alone — support is always available. 🤝"
        )

    return "\n\n".join(response_chunks)
