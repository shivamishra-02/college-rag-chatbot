# backend/vector_store.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from text_splitter import split_documents
from data_loader import load_all_data


def create_vector_store():
    print("🚀 Starting vector DB creation...")

    # Step 1: Load data
    documents = load_all_data()
    print(f"📄 Loaded documents: {len(documents)}")

    # Step 2: Chunking
    chunks = split_documents(documents)
    print(f"✂️ Chunks created: {len(chunks)}")

    # Step 3: Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Step 4: Create FAISS DB
    vector_db = FAISS.from_documents(chunks, embeddings)

    # Step 5: Save
    vector_db.save_local("faiss_index")

    print("✅ Vector DB created successfully!")

    return vector_db


if __name__ == "__main__":
    create_vector_store()