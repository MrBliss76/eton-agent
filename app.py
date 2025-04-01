import streamlit as st
from scraper import fetch_eton_exam_results

st.title("📊 Eton College Academic Results")

st.markdown("Fetching results from Eton's website...")

try:
    results = fetch_eton_exam_results()
    if not results:
        st.warning("No results found — check if the PDFs were detected.")
    else:
        for pdf_url, data in results.items():
            st.subheader(f"📄 {pdf_url}")
            for exam_type, result in data.items():
                st.markdown(f"**{exam_type}**: {result}")
except Exception as e:
    st.error(f"Oops! Something went wrong.\n\n**Error:** {e}")
