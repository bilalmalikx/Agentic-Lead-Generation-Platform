from app.tools.search_tool import web_search
from app.memory.long_term_memory import save_lead

def lead_finder_agent(state: dict):
    """
    Finds companies for the query.
    Input: state['query']
    Output: state['companies'] = [{"company": "", "website": ""}]
    """
    query = state.get("query", "")
    results = web_search(query)  # returns list of dict {"company": ..., "website": ...}

    # Save to DB
    for r in results:
        save_lead(r["company"], r["website"], email=None, industry=None)

    state["companies"] = results
    return state