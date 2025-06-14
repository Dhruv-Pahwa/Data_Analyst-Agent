import streamlit as st
import os
import pandas as pd

from utils.file_loader import load_file
from utils.llama_agent import ask_llama

st.set_page_config(page_title="Data Analyst Agent", layout="wide")
st.title("📊 Data Analyst Agent using LLaMA")

# Upload file
uploaded = st.file_uploader("📤 Upload a file", type=["csv", "xlsx", "txt", "pdf", "docx", "jpg", "png", "jpeg"])

if uploaded:
    os.makedirs("uploaded_files", exist_ok=True)
    file_path = os.path.join("uploaded_files", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.getvalue())

    data = load_file(file_path)

    if isinstance(data, pd.DataFrame):
        st.subheader("📄 Data Preview")
        st.dataframe(data.head())

        if st.button("🔍 Analyze Data"):
            prompt = (
                "You are a highly skilled data analyst.\n"
                "Analyze the following dataset. Give insights such as:\n"
                "- Trends or patterns\n"
                "- Anomalies or outliers\n"
                "- Summary statistics (mean, median, range)\n"
                "- Any potential business or economic insights.\n\n"
                f"DATA:\n{data.head(20).to_string(index=False)}"
                )

            response = ask_llama(prompt)
            st.subheader("📈 LLaMA Response")
            st.write(response)

    elif isinstance(data, str):
        st.subheader("📄 Extracted Text")
        st.text_area("Content", value=data[:2000], height=300)

        if st.button("🧠 Analyze Document"):
            prompt = f"Please analyze the following document:\n{data[:2000]}"
            response = ask_llama(prompt)
            st.subheader("📈 LLaMA Response")
            st.write(response)
    else:
        st.error("Unsupported or unreadable file.")

# 🔬 Direct API test
st.divider()
if st.button("🧪 Test LLaMA Output"):
    st.subheader("Test Prompt: What is the capital of India?")
    response = ask_llama("What is the capital of India?")
    st.write(response)
