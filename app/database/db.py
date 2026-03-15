from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.configs.settings import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

base = declarative_base()