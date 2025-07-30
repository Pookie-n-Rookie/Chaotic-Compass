from typing import TypedDict, Annotated, List, Optional
from langchain_core.messages import HumanMessage, AIMessage

class PlannerState(TypedDict):
    """State definition for the travel planner workflow"""
    messages: Annotated[List[HumanMessage | AIMessage], "messages in the conversation"]
    city: str
    interests: List[str]
    budget: str
    duration: str
    travel_style: str
    group_size: str
    accommodation_type: str
    transportation: str
    dietary_restrictions: str
    itinerary: str
    recommendations: List[str]
    alternative_plans: List[str]
    local_tips: str
    weather_considerations: str
    safety_info: str
    current_step: str
    user_satisfaction: Optional[bool]
    refinement_requested: bool