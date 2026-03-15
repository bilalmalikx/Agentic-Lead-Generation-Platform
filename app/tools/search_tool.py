import requests
from bs4 import BeautifulSoup

def web_search(query: str):
    """
    Simple web search tool (mock). 
    Returns a list of dicts: {"company": str, "website": str}
    """
    # Production me Google/Bing API ya SerpAPI use karna chahiye
    # Ye example static response for testing
    results = [
        {"company": "Tempus AI", "website": "https://www.tempus.com"},
        {"company": "Insitro", "website": "https://www.insitro.com"}
    ]
    return results