from app.services.openai_service import get_llm

def planner_agent(state: dict):
    """
    Generates a step-by-step plan for the lead generation process.
    Input: state dict with 'query'
    Output: state dict with 'plan'
    """
    llm = get_llm()

    with open("app/prompts/planner_prompt.txt", "r") as f:
        prompt_template = f.read()

    query = state.get("query", "")
    prompt = prompt_template + f"\n\nQuery: {query}"

    plan = llm.call(prompt)  # simple LLM call
    state["plan"] = plan
    return state