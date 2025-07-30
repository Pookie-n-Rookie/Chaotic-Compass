import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from state_definitions import PlannerState

# Initialize AI Model
llm = ChatGroq(
    temperature=0.1,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Prompt Templates
itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are ChaoticCompass, a wild and unpredictable travel assistant. "
               "Create a {duration} itinerary for {city} based on {interests} with a {budget} budget. "
               "Consider {group_size} travelers with {travel_style} style. "
               "Include {accommodation_type} accommodations and {transportation} transportation. "
               "Account for dietary restrictions: {dietary_restrictions}. "
               "Make it exciting, unique, and chaotic!"),
    ("human", "Create a detailed travel itinerary."),
])

recommendations_prompt = ChatPromptTemplate.from_messages([
    ("system", "Provide specific restaurant, activity, and shopping recommendations for {city} "
               "focusing on {interests}. Consider {budget} budget and {dietary_restrictions}."),
    ("human", "Give me detailed recommendations."),
])

local_tips_prompt = ChatPromptTemplate.from_messages([
    ("system", "Share insider local tips, hidden gems, and cultural insights for {city}. "
               "Include transportation hacks, local etiquette, and off-the-beaten-path suggestions."),
    ("human", "What are the best local tips?"),
])

safety_prompt = ChatPromptTemplate.from_messages([
    ("system", "Provide safety information and travel advisories for {city}. "
               "Include emergency contacts, common scams, safe areas, and health considerations."),
    ("human", "What should I know about safety?"),
])

# Node Functions
def input_city(state: PlannerState) -> PlannerState:
    print("🌍 Enter the city for your trip: ")
    city = input("Your Input: ")
    return {
        **state, 
        "city": city, 
        "current_step": "city_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Selected city: {city}")]
    }

def input_interests(state: PlannerState) -> PlannerState:
    print(f"🎯 Enter your interests for {state['city']} (comma-separated): ")
    interests = input("Your Input: ").split(",")
    return {
        **state, 
        "interests": [i.strip() for i in interests],
        "current_step": "interests_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Interests: {', '.join(interests)}")]
    }

def input_budget(state: PlannerState) -> PlannerState:
    print("💰 What's your budget range? (budget/mid-range/luxury)")
    budget = input("Your Input: ")
    return {
        **state, 
        "budget": budget,
        "current_step": "budget_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Budget: {budget}")]
    }

def input_duration(state: PlannerState) -> PlannerState:
    print("📅 How long is your trip? (1 day/3 days/1 week/2 weeks)")
    duration = input("Your Input: ")
    return {
        **state, 
        "duration": duration,
        "current_step": "duration_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Duration: {duration}")]
    }

def input_travel_style(state: PlannerState) -> PlannerState:
    print("🎒 What's your travel style? (adventurous/relaxed/cultural/party/family-friendly)")
    travel_style = input("Your Input: ")
    return {
        **state, 
        "travel_style": travel_style,
        "current_step": "style_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Travel style: {travel_style}")]
    }

def input_group_details(state: PlannerState) -> PlannerState:
    print("👥 Group size? (solo/couple/small group/large group)")
    group_size = input("Your Input: ")
    return {
        **state, 
        "group_size": group_size,
        "current_step": "group_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Group size: {group_size}")]
    }

def input_accommodation(state: PlannerState) -> PlannerState:
    print("🏨 Preferred accommodation? (hostel/hotel/airbnb/luxury resort/camping)")
    accommodation = input("Your Input: ")
    return {
        **state, 
        "accommodation_type": accommodation,
        "current_step": "accommodation_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Accommodation: {accommodation}")]
    }

def input_transportation(state: PlannerState) -> PlannerState:
    print("🚗 Preferred transportation? (public transport/rental car/walking/bike/mixed)")
    transportation = input("Your Input: ")
    return {
        **state, 
        "transportation": transportation,
        "current_step": "transport_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Transportation: {transportation}")]
    }

def input_dietary_restrictions(state: PlannerState) -> PlannerState:
    print("🍽️ Any dietary restrictions? (none/vegetarian/vegan/gluten-free/halal/kosher/other)")
    dietary = input("Your Input: ")
    return {
        **state, 
        "dietary_restrictions": dietary,
        "current_step": "dietary_selected",
        "messages": state["messages"] + [HumanMessage(content=f"Dietary restrictions: {dietary}")]
    }

def create_main_itinerary(state: PlannerState) -> PlannerState:
    print("\n🔥 Creating your chaotic itinerary...")
    
    prompt_vars = {
        "city": state["city"],
        "interests": ', '.join(state["interests"]),
        "budget": state.get("budget", "mid-range"),
        "duration": state.get("duration", "3 days"),
        "travel_style": state.get("travel_style", "adventurous"),
        "group_size": state.get("group_size", "solo"),
        "accommodation_type": state.get("accommodation_type", "hotel"),
        "transportation": state.get("transportation", "mixed"),
        "dietary_restrictions": state.get("dietary_restrictions", "none")
    }
    
    response = llm.invoke(itinerary_prompt.format_messages(**prompt_vars))
    itinerary = response.content
    
    print(f"\n📋 Main Itinerary:\n{itinerary}")
    
    return {
        **state, 
        "itinerary": itinerary,
        "current_step": "itinerary_created",
        "messages": state["messages"] + [AIMessage(content=itinerary)]
    }

def generate_recommendations(state: PlannerState) -> PlannerState:
    print("\n🎯 Generating specific recommendations...")
    
    response = llm.invoke(recommendations_prompt.format_messages(
        city=state["city"],
        interests=', '.join(state["interests"]),
        budget=state.get("budget", "mid-range"),
        dietary_restrictions=state.get("dietary_restrictions", "none")
    ))
    
    recommendations = response.content.split('\n')
    recommendations = [r.strip() for r in recommendations if r.strip()]
    
    print(f"\n💡 Recommendations:\n{chr(10).join(recommendations[:5])}")
    
    return {
        **state, 
        "recommendations": recommendations,
        "current_step": "recommendations_generated",
        "messages": state["messages"] + [AIMessage(content=response.content)]
    }

def generate_local_tips(state: PlannerState) -> PlannerState:
    print("\n🗝️ Gathering local insider tips...")
    
    response = llm.invoke(local_tips_prompt.format_messages(city=state["city"]))
    local_tips = response.content
    
    print(f"\n🔍 Local Tips:\n{local_tips}")
    
    return {
        **state, 
        "local_tips": local_tips,
        "current_step": "tips_generated",
        "messages": state["messages"] + [AIMessage(content=local_tips)]
    }

def generate_safety_info(state: PlannerState) -> PlannerState:
    print("\n🛡️ Compiling safety information...")
    
    response = llm.invoke(safety_prompt.format_messages(city=state["city"]))
    safety_info = response.content
    
    print(f"\n⚠️ Safety Info:\n{safety_info}")
    
    return {
        **state, 
        "safety_info": safety_info,
        "current_step": "safety_generated",
        "messages": state["messages"] + [AIMessage(content=safety_info)]
    }

def create_alternative_plans(state: PlannerState) -> PlannerState:
    print("\n🔄 Creating alternative plans...")
    
    alternatives = []
    alternative_styles = ["budget-focused", "luxury", "off-the-beaten-path"]
    
    for style in alternative_styles:
        alt_prompt = ChatPromptTemplate.from_messages([
            ("system", f"Create a {style} alternative itinerary for {state['city']} "
                      f"based on {', '.join(state['interests'])}. Make it distinct from mainstream tourism."),
            ("human", "Create an alternative travel plan."),
        ])
        
        response = llm.invoke(alt_prompt.format_messages())
        alternatives.append(f"**{style.title()} Plan:**\n{response.content}")
    
    print(f"\n🎲 Alternative Plans Generated: {len(alternatives)} options")
    
    return {
        **state, 
        "alternative_plans": alternatives,
        "current_step": "alternatives_created",
        "messages": state["messages"] + [AIMessage(content=f"Generated {len(alternatives)} alternative plans")]
    }

def check_satisfaction(state: PlannerState) -> PlannerState:
    print("\n😊 Are you satisfied with your travel plan? (yes/no/modify)")
    satisfaction = input("Your Input: ").lower()
    
    is_satisfied = satisfaction in ["yes", "y", "satisfied", "good", "great"]
    needs_refinement = satisfaction in ["no", "modify", "change", "different"]
    
    return {
        **state, 
        "user_satisfaction": is_satisfied,
        "refinement_requested": needs_refinement,
        "current_step": "satisfaction_checked",
        "messages": state["messages"] + [HumanMessage(content=f"Satisfaction: {satisfaction}")]
    }

def refine_itinerary(state: PlannerState) -> PlannerState:
    print("\n🔧 What would you like to modify? (activities/budget/style/duration/other)")
    modification = input("Your Input: ")
    
    print(f"Please specify your new preference for {modification}:")
    new_preference = input("Your Input: ")
    
    # Update the relevant state field based on modification type
    updates = {}
    if "budget" in modification.lower():
        updates["budget"] = new_preference
    elif "style" in modification.lower():
        updates["travel_style"] = new_preference
    elif "duration" in modification.lower():
        updates["duration"] = new_preference
    elif "activities" in modification.lower() or "interests" in modification.lower():
        updates["interests"] = [i.strip() for i in new_preference.split(",")]
    
    # Regenerate itinerary with new preferences
    prompt_vars = {
        "city": state["city"],
        "interests": ', '.join(updates.get("interests", state["interests"])),
        "budget": updates.get("budget", state.get("budget", "mid-range")),
        "duration": updates.get("duration", state.get("duration", "3 days")),
        "travel_style": updates.get("travel_style", state.get("travel_style", "adventurous")),
        "group_size": state.get("group_size", "solo"),
        "accommodation_type": state.get("accommodation_type", "hotel"),
        "transportation": state.get("transportation", "mixed"),
        "dietary_restrictions": state.get("dietary_restrictions", "none")
    }
    
    response = llm.invoke(itinerary_prompt.format_messages(**prompt_vars))
    refined_itinerary = response.content
    
    print(f"\n✨ Refined Itinerary:\n{refined_itinerary}")
    
    return {
        **state, 
        **updates,
        "itinerary": refined_itinerary,
        "refinement_requested": False,
        "current_step": "itinerary_refined",
        "messages": state["messages"] + [
            HumanMessage(content=f"Requested modification: {modification} -> {new_preference}"),
            AIMessage(content=refined_itinerary)
        ]
    }

def finalize_plan(state: PlannerState) -> PlannerState:
    print("\n🎉 Finalizing your chaotic travel adventure!")
    print("=" * 50)
    print("FINAL TRAVEL PLAN")
    print("=" * 50)
    print(f"📍 Destination: {state['city']}")
    print(f"🎯 Interests: {', '.join(state['interests'])}")
    print(f"💰 Budget: {state.get('budget', 'Not specified')}")
    print(f"📅 Duration: {state.get('duration', 'Not specified')}")
    print(f"🎒 Style: {state.get('travel_style', 'Not specified')}")
    print("\n📋 ITINERARY:")
    print(state['itinerary'])
    
    if state.get('recommendations'):
        print(f"\n💡 TOP RECOMMENDATIONS:")
        for i, rec in enumerate(state['recommendations'][:3], 1):
            print(f"{i}. {rec}")
    
    if state.get('local_tips'):
        print(f"\n🗝️ LOCAL INSIDER TIPS:")
        print(state['local_tips'][:300] + "..." if len(state['local_tips']) > 300 else state['local_tips'])
    
    print("\n🌟 Have an amazing chaotic adventure!")
    
    return {
        **state, 
        "current_step": "plan_finalized",
        "messages": state["messages"] + [AIMessage(content="Travel plan finalized! Ready for adventure!")]
    }