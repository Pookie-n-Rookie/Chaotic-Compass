from workflow_engine import create_workflow
from state_definitions import PlannerState

def get_initial_state() -> PlannerState:
    """Initialize the state for CLI workflow"""
    return {
        "messages": [],
        "city": "",
        "interests": [],
        "budget": "",
        "duration": "",
        "travel_style": "",
        "group_size": "",
        "accommodation_type": "",
        "transportation": "",
        "dietary_restrictions": "",
        "itinerary": "",
        "recommendations": [],
        "alternative_plans": [],
        "local_tips": "",
        "weather_considerations": "",
        "safety_info": "",
        "current_step": "",
        "user_satisfaction": None,
        "refinement_requested": False
    }

def run_cli_planner():
    """Run the full LangGraph workflow in CLI mode"""
    app = create_workflow()
    initial_state = get_initial_state()
    
    print("\n🌟 Starting your chaotic travel planning journey...")
    print("Follow the prompts to create your ultimate travel itinerary!")
    print("-" * 60)
    
    try:
        final_state = app.invoke(initial_state)
        print("\n🎉 Your adventure plan is complete!")
        print("Safe travels and enjoy your chaotic adventure! 🌍✨")
    except KeyboardInterrupt:
        print("\n\n🚫 Planning interrupted. Come back anytime for your chaotic adventure!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again or use the web interface.")