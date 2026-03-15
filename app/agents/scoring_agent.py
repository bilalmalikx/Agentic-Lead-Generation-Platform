from app.services.openai_service import get_llm
import json

def scoring_agent(state: dict):
    llm = get_llm()
    with open("app/prompts/scoring_prompt.txt") as f:
        prompt_template = f.read()

    leads = state.get("emails", [])
    prompt = prompt_template + f"\n\nLeads: {json.dumps(leads)}"
    scored = llm.call(prompt)
    # Assume LLM returns JSON array
    state["scored_leads"] = json.loads(scored)
    return state