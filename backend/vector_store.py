# backend/vector_store.py

# FAISS = Facebook AI Similarity Search (fast vector DB)
from langchain_community.vectorstores import FAISS

# Embedding model (HuggingFace - free)
from langchain_community.embeddings import HuggingFaceEmbeddings

# Apna chunking logic import
from text_splitter import split_documents
from data_loader import load_all_data


def create_vector_store():
    """
    Ye function:
    1. Data load karega
    2. Chunk karega
    3. Embeddings banayega
    4. Vector DB me store karega
    """

    # 🔹 Step 1: Load all documents
    documents = load_all_data()

    # 🔹 Step 2: Convert into chunks
    chunks = split_documents(documents)

    # 🔹 Step 3: Embedding model load karna
    # ye free hai (OpenAI ka paisa nahi lagega)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 🔹 Step 4: FAISS vector DB banana
    vector_db = FAISS.from_documents(chunks, embeddings)

    # 🔹 Step 5: Save locally (important)
    vector_db.save_local("faiss_index")

    print("\n✅ Vector DB created and saved successfully!")

    return vector_db


if __name__ == "__main__":
    create_vector_store()