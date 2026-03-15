from langchain_openai import ChatOpenAI


def get_llm():
    llm = ChatOpenAI(
        model="gpt-4-0613",
        temperature=0.7,
    )
    return llm