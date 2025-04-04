import pdfplumber
import requests
import io
import re

def extract_text_from_pdf(url):
    r = requests.get(url)
    with pdfplumber.open(io.BytesIO(r.content)) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

def parse_exam_results(text):
    results = {}

    if "GCSE" in text:
        match = re.search(r"(GCSE.*?)(\d+%.*?A\*)", text, re.DOTALL)
        if match:
            results["GCSE"] = match.group(2)

    if "A-Level" in text:
        match = re.search(r"(A-Level.*?)(\d+%.*?A\*)", text, re.DOTALL)
        if match:
            results["A-Level"] = match.group(2)

    return results

