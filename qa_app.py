import streamlit as st
from transformers import pipeline

# Set up the QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# App title
st.title("📖 Question Answering Bot")
st.write("Enter a paragraph and ask questions based on it using a pre-trained Transformer model.")

# Input paragraph
context = st.text_area("📝 Enter your paragraph (context):", height=200, key="context_input")

# Add a horizontal line
st.markdown("---")

# Question input and result in columns
col1, col2 = st.columns([2, 3])

with col1:
    question = st.text_input("❓ Ask a question about the paragraph:", key="question_input")

with col2:
    if question and context:
        result = qa_pipeline(question=question, context=context)
        st.success(f"**Answer:** {result['answer']}")
    elif question:
        st.warning("⚠️ Please enter a paragraph above before asking questions.")
