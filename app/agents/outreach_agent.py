from app.services.openai_service import get_llm
import json

def outreach_agent(state: dict):
    llm = get_llm()
    with open("app/prompts/outreach_prompt.txt") as f:
        prompt_template = f.read()

    leads = state.get("scored_leads", [])
    prompt = prompt_template + f"\n\nLeads: {json.dumps(leads)}"
    messages = llm.call(prompt)
    state["outreach_messages"] = json.loads(messages)
    return state