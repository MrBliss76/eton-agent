from utils import extract_text_from_pdf, parse_exam_results
import requests
from bs4 import BeautifulSoup

SCHOOLS = {
    "Eton College": "https://www.etoncollege.com/about-us/exam-results/",
    "Harrow School": "https://www.harrowschool.org.uk/academic/examination-results",
    "Winchester College": "https://www.winchestercollege.org/academic/results",
    "Cheltenham Ladies’ College": "https://www.cheltladiescollege.org/information/results/",
    "Westminster School": "https://www.westminster.org.uk/exam-results/"
}

def fetch_results_for_school(name):
    url = SCHOOLS.get(name)
    if not url:
        return {}

    try:
        # Try to extract PDFs
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        pdf_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    text = a.get_text(strip=True).lower()
    if ".pdf" in href.lower() and any(keyword in href.lower() + text for keyword in ["exam", "results", "a-level", "gcse", "ib"]):
        if not href.startswith("http"):
            href = url.rstrip("/") + "/" + href.lstrip("/")
        pdf_links.append(href)

        results = {}

        for link in pdf_links[:1]:  # limit to 1 for speed
            if not link.startswith("http"):
                link = url.rstrip("/") + "/" + link.lstrip("/")
            text = extract_text_from_pdf(link)
            parsed = parse_exam_results(text)
            results[link] = parsed

        return results if results else {"No results found": {}}

    except Exception as e:
        return {"Error": str(e)}
