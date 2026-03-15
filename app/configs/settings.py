from pydantic import BaseModel

class Settings(BaseModel):
    OPEN_API_KEY: str
    LANGSMITH_API_KEY: str
    DATABASE_URL: str

    class config:
        env_file = ".env"

settings = Settings()