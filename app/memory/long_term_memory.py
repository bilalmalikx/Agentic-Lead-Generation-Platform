from app.database.db import SessionLocal
from app.database.models import Lead


class save_lead(company_name, website, email, industry):
    db = SessionLocal()

    lead = Lead(
        company_name=company_name,
        website=website,
        email=email,
        industry=industry
    )

    db.add(lead)
    db.commit() 
    db.close()