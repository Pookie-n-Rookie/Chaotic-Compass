from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from app.itinerary import generate_itinerary

# Define state
class PlannerState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], "messages in the conversation"]
    city: str
    interests: List[str]
    itinerary: str

# User input nodes
def input_city(state: PlannerState) -> PlannerState:
    print("Enter the city for your trip: ")
    city = input("Your Input: ")
    return {**state, "city": city, "messages": state["messages"] + [HumanMessage(content=city)]}

def input_interests(state: PlannerState) -> PlannerState:
    print(f"Enter your interests for {state['city']} (comma-separated): ")
    interests = input("Your Input: ").split(",")
    return {**state, "interests": [i.strip() for i in interests], "messages": state["messages"] + [HumanMessage(content=', '.join(interests))]}

def create_itinerary(state: PlannerState) -> PlannerState:
    itinerary = generate_itinerary(state["city"], ', '.join(state["interests"]))
    print("\nFinal Itinerary: \n", itinerary)
    return {**state, "itinerary": itinerary, "messages": state["messages"] + [AIMessage(content=itinerary)]}

# LangGraph Workflow
workflow = StateGraph(PlannerState)
workflow.add_node("input_city", input_city)
workflow.add_node("input_interests", input_interests)
workflow.add_node("create_itinerary", create_itinerary)

workflow.set_entry_point("input_city")
workflow.add_edge("input_city", "input_interests")
workflow.add_edge("input_interests", "create_itinerary")
workflow.add_edge("create_itinerary", END)

app = workflow.compile()
