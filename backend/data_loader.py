from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import pandas as pd

# 📄 Load PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


# 📊 Load CSV
def load_csv(file_path):
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
        
        doc = Document(page_content=content)
        documents.append(doc)
    
    return documents


# 🔥 Combine
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
    print(docs[0].page_content[:300])