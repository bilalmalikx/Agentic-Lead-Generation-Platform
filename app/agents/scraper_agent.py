from app.tools.website_scraper import scrape_website

def scraper_agent(state: dict):
    """
    Scrape websites of all companies.
    """
    scraped_data = []
    for company in state.get("companies", []):
        url = company.get("website")
        if url:
            text = scrape_website(url)
            scraped_data.append({"company": company["company"], "text": text})

    state["scraped_data"] = scraped_data
    return state