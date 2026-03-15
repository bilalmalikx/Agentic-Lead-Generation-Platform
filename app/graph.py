from langgraph.graph import Graph
from app.agents.planner_agent import planner_agent
from app.agents.lead_finder_agent import lead_finder_agent
from app.agents.scraper_agent import scraper_agent
from app.agents.enrichment_agent import enrichment_agent
from app.agents.scoring_agent import scoring_agent
from app.agents.outreach_agent import outreach_agent

graph = Graph()

graph.add_node("planner", planner_agent)
graph.add_node("lead_finder", lead_finder_agent)
graph.add_node("scraper", scraper_agent)
graph.add_node("enrichment", enrichment_agent)
graph.add_node("scoring", scoring_agent)
graph.add_node("outreach", outreach_agent)

# Connect nodes
graph.add_edge("planner", "lead_finder")
graph.add_edge("lead_finder", "scraper")
graph.add_edge("scraper", "enrichment")
graph.add_edge("enrichment", "scoring")
graph.add_edge("scoring", "outreach")

graph = graph.compile()