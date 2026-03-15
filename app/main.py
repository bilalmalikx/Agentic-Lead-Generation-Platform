from fastapi import FastAPI
from app.graph import graph

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Lead Generation Agent Running"}

@app.post("/generate-leads")
def generate_leads(query: str):

    result = graph.invoke({
        "query": query,
        "companies": [],
        "scraped_data": [],
        "emails": [],
        "scored_leads": [],
        "outreach_messages": []
    })

    return result