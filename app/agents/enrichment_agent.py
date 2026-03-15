from app.tools.email_extractor import extract_emails
from app.memory.long_term_memory import save_lead

def enrichment_agent(state: dict):
    enriched = []
    for item in state.get("scraped_data", []):
        company = item["company"]
        text = item["text"]
        emails = extract_emails(text)
        enriched.append({"company": company, "emails": emails})

        # Update DB
        for email in emails:
            save_lead(company, website=None, email=email, industry=None)

    state["emails"] = enriched
    return state