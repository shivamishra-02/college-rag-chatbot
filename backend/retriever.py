# backend/retriever.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_vector_db():
    """
    FAISS vector DB load karta hai
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db


def query_data(query):
    """
    Query ke basis pe relevant chunks nikaalta hai
    """

    vector_db = load_vector_db()

    # 🔥 STEP 1: WITHOUT FILTER (debug ke liye)
    retriever = vector_db.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    results = retriever.invoke(query)

    print("\n🔍 Retrieved Chunks (WITHOUT FILTER):\n")

    for i, doc in enumerate(results):
        print(f"\n--- Result {i+1} ---\n")
        print(doc.page_content)
        print("Metadata:", doc.metadata)

    # 🔥 STEP 2: WITH FILTER (actual use)
    retriever_filtered = vector_db.as_retriever(
        search_kwargs={
            "k": 3,
            "filter": {"source": "college_info"}
        }
    )

    filtered_results = retriever_filtered.invoke(query)

    print("\n🎯 Retrieved Chunks (WITH FILTER - college_info):\n")

    if not filtered_results:
        print("⚠️ No results found with filter (check metadata or rebuild vector DB)\n")

    for i, doc in enumerate(filtered_results):
        print(f"\n--- Filtered Result {i+1} ---\n")
        print(doc.page_content)
        print("Metadata:", doc.metadata)


if __name__ == "__main__":
    
    query = "What is hostel fee?"
    query_data(query)