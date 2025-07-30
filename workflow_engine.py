from langgraph.graph import StateGraph, END
from state_definitions import PlannerState
from workflow_nodes import (
    input_city, input_interests, input_budget, input_duration,
    input_travel_style, input_group_details, input_accommodation,
    input_transportation, input_dietary_restrictions, create_main_itinerary,
    generate_recommendations, generate_local_tips, generate_safety_info,
    create_alternative_plans, check_satisfaction, refine_itinerary, finalize_plan
)

def should_refine(state: PlannerState) -> str:
    """Conditional routing for refinement or finalization"""
    if state.get("refinement_requested", False):
        return "refine_itinerary"
    elif state.get("user_satisfaction", False):
        return "finalize_plan"
    else:
        return "finalize_plan"  # Default to finalization

def create_workflow():
    """Create and compile the LangGraph workflow"""
    workflow = StateGraph(PlannerState)

    # Add all nodes
    workflow.add_node("input_city", input_city)
    workflow.add_node("input_interests", input_interests)
    workflow.add_node("input_budget", input_budget)
    workflow.add_node("input_duration", input_duration)
    workflow.add_node("input_travel_style", input_travel_style)
    workflow.add_node("input_group_details", input_group_details)
    workflow.add_node("input_accommodation", input_accommodation)
    workflow.add_node("input_transportation", input_transportation)
    workflow.add_node("input_dietary_restrictions", input_dietary_restrictions)
    workflow.add_node("create_main_itinerary", create_main_itinerary)
    workflow.add_node("generate_recommendations", generate_recommendations)
    workflow.add_node("generate_local_tips", generate_local_tips)
    workflow.add_node("generate_safety_info", generate_safety_info)
    workflow.add_node("create_alternative_plans", create_alternative_plans)
    workflow.add_node("check_satisfaction", check_satisfaction)
    workflow.add_node("refine_itinerary", refine_itinerary)
    workflow.add_node("finalize_plan", finalize_plan)

    # Set entry point
    workflow.set_entry_point("input_city")

    # Sequential flow for basic information gathering
    workflow.add_edge("input_city", "input_interests")
    workflow.add_edge("input_interests", "input_budget")
    workflow.add_edge("input_budget", "input_duration")
    workflow.add_edge("input_duration", "input_travel_style")
    workflow.add_edge("input_travel_style", "input_group_details")
    workflow.add_edge("input_group_details", "input_accommodation")
    workflow.add_edge("input_accommodation", "input_transportation")
    workflow.add_edge("input_transportation", "input_dietary_restrictions")

    # Main itinerary creation
    workflow.add_edge("input_dietary_restrictions", "create_main_itinerary")

    # Parallel processing of additional information
    workflow.add_edge("create_main_itinerary", "generate_recommendations")
    workflow.add_edge("generate_recommendations", "generate_local_tips")
    workflow.add_edge("generate_local_tips", "generate_safety_info")
    workflow.add_edge("generate_safety_info", "create_alternative_plans")

    # Satisfaction check and refinement loop
    workflow.add_edge("create_alternative_plans", "check_satisfaction")
    workflow.add_conditional_edges(
        "check_satisfaction",
        should_refine,
        {
            "refine_itinerary": "refine_itinerary",
            "finalize_plan": "finalize_plan"
        }
    )

    # Refinement loop
    workflow.add_edge("refine_itinerary", "check_satisfaction")
    workflow.add_edge("finalize_plan", END)

    # Compile the workflow
    return workflow.compile()