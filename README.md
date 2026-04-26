# 🎓 College RAG Chatbot (NIET Based)

An AI-powered chatbot built using **Retrieval-Augmented Generation (RAG)** that answers queries related to college data such as courses, fees, rules, and student information.

---

## 🚀 Features

* 📄 Extracts data from **PDF (college info)** and **CSV (student records)**
* 🔍 Uses **FAISS Vector Database** for semantic search
* 🧠 Powered by **Google Gemini (LLM)**
* 💬 Interactive **Streamlit Chat UI**
* ⚡ Supports scalable backend using **FastAPI (API-based architecture)**
* 🎯 Context-aware responses (no hallucination, answers from data only)

---

## 🧠 How It Works (RAG Pipeline)

1. Load data from PDF & CSV
2. Split into chunks
3. Convert into embeddings
4. Store in FAISS vector DB
5. Retrieve relevant chunks based on query
6. Send context + question to LLM (Gemini)
7. Generate final answer

---

## 🏗️ Architecture

```
                ┌───────────────┐
                │   User (UI)   │
                └──────┬────────┘
                       │
                       ▼
            ┌────────────────────┐
            │  Streamlit Frontend │
            └────────┬───────────┘
                     │ API Call
                     ▼
            ┌────────────────────┐
            │   FastAPI Backend  │
            └────────┬───────────┘
                     │
                     ▼
            ┌────────────────────┐
            │   RAG Pipeline     │
            │ (Retriever + LLM)  │
            └────────┬───────────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
  FAISS Vector DB         Gemini LLM (2.5 Flash)
        │                         │
        └────────────┬────────────┘
                     ▼
                Final Answer
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **LLM:** Google Gemini (2.5 Flash)
* **Vector DB:** FAISS
* **Embeddings:** HuggingFace (MiniLM)
* **Language:** Python

---

## 📁 Project Structure

```
college-rag-chatbot/
│
├── backend/
│   ├── data_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   └── api.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── raw/
│       ├── niet_info.pdf
│       └── students.csv
│
├── faiss_index/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```bash
git clone <your-repo-link>
cd college-rag-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create `.env` file in root:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5️⃣ Create Vector Database

```bash
python backend/vector_store.py
```

---

### 6️⃣ Run Application

#### Option 1: Direct Streamlit (Simple)

```bash
streamlit run frontend/app.py
```

#### Option 2: Full Stack (Recommended)

Start Backend:

```bash
uvicorn backend.api:app --reload
```

Start Frontend:

```bash
streamlit run frontend/app.py
```

---

## 🎯 Example Queries

* What is the fee structure for B.Tech?
* Tell me about NIET college
* Who has highest marks?
* Student details of Rahul Sharma

---

## 🔥 Future Improvements

* ✅ Source citation (PDF/CSV reference)
* 🎤 Voice-based queries
* 🌐 Deployment on AWS / GCP
* 📱 Mobile-friendly UI
* 🧠 Query classification (smart filtering)

---

## 👨‍💻 Author

**Shivam Mishra**
🔗 LinkedIn: https://www.linkedin.com/in/shivam-mishra-3a741b253/

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
