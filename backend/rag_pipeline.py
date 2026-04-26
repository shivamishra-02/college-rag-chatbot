# backend/rag_pipeline.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Direct Gemini SDK (same as your working code)
from google import genai
import os
from dotenv import load_dotenv


# 🔐 Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def load_vector_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db


def create_rag_pipeline():
    vector_db = load_vector_db()

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    def rag_chain(question):
        # 🔍 Step 1: Retrieve context
        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        # 🧠 Step 2: Prompt
        prompt = f"""
You are a helpful college assistant.

Answer ONLY using the given context.
If answer is not present, say "Not found in database".

Context:
{context}

Question:
{question}
"""

        # 🔥 Step 3: Gemini call (same working model)
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    return rag_chain


if __name__ == "__main__":

    rag = create_rag_pipeline()

    print("\n🤖 College Chatbot Ready (Gemini 2.5 Flash)!\n")

    while True:
        query = input("Ask something: ")

        if query.lower() == "exit":
            break

        answer = rag(query)

        print("\n💬 Answer:\n")
        print(answer)
        print("\n" + "-"*50 + "\n")