import streamlit as st
from scraper import fetch_eton_exam_results

st.title("📊 Eton College Academic Results")

results = fetch_eton_exam_results()

for pdf_url, data in results.items():
    st.subheader(f"📄 {pdf_url}")
    for exam_type, result in data.items():
        st.markdown(f"**{exam_type}**: {result}")
