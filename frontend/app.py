# frontend/app.py

import streamlit as st
import sys
import os

# backend import karne ke liye path add
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.rag_pipeline import create_rag_pipeline


# 🔥 Page config
st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Chatbot")
st.write("Ask anything about your college 📚")

# 🔹 RAG pipeline load (once)
@st.cache_resource
def load_rag():
    return create_rag_pipeline()

rag = load_rag()


# 🔹 Chat history store
if "messages" not in st.session_state:
    st.session_state.messages = []


# 🔹 Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# 🔹 User input
user_input = st.chat_input("Ask your question...")

if user_input:
    
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    with st.spinner("Thinking... 🤔"):
        answer = rag(user_input)

    # Show bot response
    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})