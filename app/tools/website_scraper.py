# app/tools/website_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_website(url: str):
    """
    Scrapes visible text from a given URL
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get all text from <p> tags as example
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return text

    except Exception as e:
        return ""