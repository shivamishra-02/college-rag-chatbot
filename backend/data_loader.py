# backend/data_loader.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import pandas as pd


# 📄 Load PDF
def load_pdf(file_path):
    """
    PDF ko load karta hai aur metadata add karta hai
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # 🔥 metadata add (important for filtering)
    for doc in documents:
        doc.metadata = {"source": "college_info"}

    return documents


# 📊 Load CSV
def load_csv(file_path):
    """
    CSV ko row-wise documents me convert karta hai
    """
    df = pd.read_csv(file_path)

    documents = []

    for _, row in df.iterrows():

        content = f"""
        Student ID: {row['student_id']}
        Name: {row['name']}
        Branch: {row['branch']}
        Year: {row['year']}
        Attendance: {row['attendance']}%
        Marks: {row['marks']}
        Hostel: {row['hostel']}
        """

        # 🔥 metadata add yahin hoga
        doc = Document(
            page_content=content,
            metadata={"source": "student_data"}
        )

        documents.append(doc)

    return documents


# 🔥 Combine PDF + CSV
def load_all_data():
    pdf_docs = load_pdf("data/raw/niet_info.pdf")
    csv_docs = load_csv("data/raw/students.csv")

    all_docs = pdf_docs + csv_docs

    print(f"PDF Docs: {len(pdf_docs)}")
    print(f"CSV Docs: {len(csv_docs)}")
    print(f"Total Docs: {len(all_docs)}")

    return all_docs


if __name__ == "__main__":
    docs = load_all_data()
    print("\n--- SAMPLE ---\n")
    print(docs[0].page_content[:300])