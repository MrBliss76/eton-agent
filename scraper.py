import requests
from bs4 import BeautifulSoup
from utils import extract_text_from_pdf, parse_exam_results

def fetch_eton_exam_results():
    url = "https://www.etoncollege.com/about-us/exam-results/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.endswith(".pdf"):
            if not href.startswith("http"):
                href = "https://www.etoncollege.com" + href
            pdf_links.append(href)

    results = {}
    for link in pdf_links:
        text = extract_text_from_pdf(link)
        results[link] = parse_exam_results(text)

    return results

