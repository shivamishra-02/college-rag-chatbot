# backend/retriever.py

# FAISS DB
from langchain_community.vectorstores import FAISS

# ✅ New embeddings import (updated)
from langchain_huggingface import HuggingFaceEmbeddings


def load_vector_db():
    """
    Load saved FAISS vector database
    """

    # 🔹 Embedding model (same hona chahiye jo create time pe use hua tha)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 🔹 Load FAISS DB
    vector_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db


def query_data(query):
    """
    Query ke basis pe relevant chunks retrieve karega
    """

    # Step 1: Load DB
    vector_db = load_vector_db()

    # Step 2: Create retriever
    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    # 🔥 Step 3: NEW METHOD (invoke)
    results = retriever.invoke(query)

    print("\n🔍 Retrieved Chunks:\n")

    # Step 4: Print results
    for i, doc in enumerate(results):
        print(f"\n--- Result {i+1} ---\n")
        print(doc.page_content)


if __name__ == "__main__":
    
    query = "What is hostel fee?"
    query_data(query)