import requests
from bs4 import BeautifulSoup

def fetch_eton_exam_results():
    url = "https://www.etoncollege.com/about-us/exam-results/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = {}

    # Extract content from paragraphs or list items
    for p in soup.find_all(["p", "li"]):
        text = p.get_text(strip=True)
        if any(keyword in text.lower() for keyword in ["gcse", "a-level", "ib", "results", "grades"]):
            results.setdefault("Eton Results", []).append(text)

    return results
