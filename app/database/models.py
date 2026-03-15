from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base

class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String)
    website = Column(String)
    email = Column(String)

    industry = Column(String)

    lead_score = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)