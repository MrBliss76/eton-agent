import streamlit as st
from scraper import fetch_eton_exam_results

st.title("📊 Eton College Academic Results")
st.markdown("Fetching results from Eton’s website...")

try:
    results = fetch_eton_exam_results()
    if not results:
        st.warning("No results found — check if content structure changed.")
    else:
        for section, lines in results.items():
            st.subheader(section)
            for line in lines:
                st.markdown(f"- {line}")
except Exception as e:
    st.error(f"Error: {e}")
