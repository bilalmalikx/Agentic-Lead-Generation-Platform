from typing import TypedDict, List

class LeadGenState(TypedDict):

    query: str

    companies: List[str]

    scraped_data: List[str]

    emails: List[str]

    scored_leads: List[dict]

    outreach_messages: List[str]