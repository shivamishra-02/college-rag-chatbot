# backend/text_splitter.py

# RecursiveCharacterTextSplitter ek smart splitter hai
# ye sentences aur paragraphs ka respect karta hai
from langchain_text_splitters import RecursiveCharacterTextSplitter

# hum apna data_loader import kar rahe hain
from data_loader import load_all_data


def split_documents(documents):
    """
    Ye function documents ko chhote chunks me todta hai
    """

    # 🔥 Chunking strategy define karte hain
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,        # ek chunk me max 500 characters
        chunk_overlap=100      # overlap rakhenge taaki context lost na ho
    )

    # documents ko split karna
    chunks = splitter.split_documents(documents)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    return chunks


if __name__ == "__main__":
    
    # Step 1: Sare documents load karo (PDF + CSV)
    docs = load_all_data()

    # Step 2: Unko chunks me tod do
    chunks = split_documents(docs)

    # Step 3: Sample chunk print karo (samajhne ke liye)
    print("\n--- SAMPLE CHUNK ---\n")
    print(chunks[0].page_content)