import os
from typing import TypedDict, Annotated, List, Optional
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
import gradio as gr
from dotenv import load_dotenv
import random

load_dotenv()

class TravelPlanner:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0.1,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )
        self.session_history = []
        self._setup_prompts()
    
    def _setup_prompts(self):
        """Initialize all prompt templates"""
        self.itinerary_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are ChaoticCompass, a wild and unpredictable travel assistant. "
                       "Create a {duration} itinerary for {city} based on {interests} with a {budget} budget. "
                       "Consider {group_size} travelers with {travel_style} style. "
                       "Include {accommodation_type} accommodations and {transportation} transportation. "
                       "Account for dietary restrictions: {dietary_restrictions}. "
                       "Make it exciting, unique, and chaotic!"),
            ("human", "Create a detailed travel itinerary."),
        ])
        
        self.recommendations_prompt = ChatPromptTemplate.from_messages([
            ("system", "Provide specific restaurant, activity, and shopping recommendations for {city} "
                       "focusing on {interests}. Consider {budget} budget and {dietary_restrictions}."),
            ("human", "Give me detailed recommendations."),
        ])
        
        self.local_tips_prompt = ChatPromptTemplate.from_messages([
            ("system", "Share insider local tips, hidden gems, and cultural insights for {city}. "
                       "Include transportation hacks, local etiquette, and off-the-beaten-path suggestions."),
            ("human", "What are the best local tips?"),
        ])
        
        self.safety_prompt = ChatPromptTemplate.from_messages([
            ("system", "Provide safety information and travel advisories for {city}. "
                       "Include emergency contacts, common scams, safe areas, and health considerations."),
            ("human", "What should I know about safety?"),
        ])
    
    def generate_itinerary(self, city: str, interests: str, budget: str = "mid-range", 
                          duration: str = "3 days", travel_style: str = "adventurous"):
        """Generate main travel itinerary"""
        prompt_vars = {
            "city": city,
            "interests": interests,
            "budget": budget,
            "duration": duration,
            "travel_style": travel_style,
            "group_size": "solo",
            "accommodation_type": "hotel",
            "transportation": "mixed",
            "dietary_restrictions": "none"
        }
        
        response = self.llm.invoke(self.itinerary_prompt.format_messages(**prompt_vars))
        return response.content
    
    def generate_alternative_plans(self, city: str, interests: str, duration: str, travel_style: str):
        """Generate alternative travel plans"""
        alt_prompt = ChatPromptTemplate.from_messages([
            ("system", f"Create 2 alternative {duration} itineraries for {city} with different themes. "
                      f"One budget-focused, one luxury-focused. Consider {interests} and {travel_style} style."),
            ("human", "Create alternative plans."),
        ])
        response = self.llm.invoke(alt_prompt.format_messages())
        return response.content
    
    def generate_local_tips(self, city: str):
        """Generate local insider tips"""
        response = self.llm.invoke(self.local_tips_prompt.format_messages(city=city))
        return response.content
    
    def generate_safety_info(self, city: str):
        """Generate safety information"""
        response = self.llm.invoke(self.safety_prompt.format_messages(city=city))
        return response.content
    
    def get_dynamic_suggestion(self, city: str, interests: str):
        """Get a single dynamic suggestion for follow-up"""
        suggestions = [
            f"What are some must-try dishes in {city}?",
            f"Add a hidden gem in {city}",
            f"Suggest an adventurous activity in {city}",
            f"Include a cultural activity in {city}",
            f"Best local transportation tips for {city}",
            f"Safety considerations for {city}"
        ]
        return random.choice(suggestions)
    
    def handle_follow_up(self, suggestion: str, itinerary: str, city: str, interests: str):
        """Handle follow-up suggestions"""
        added_tip = f"\n\n---\n\n**{suggestion}**\n"
        
        if "dish" in suggestion:
            added_tip += f"🍽 Try some local food markets or iconic dishes from {city}!"
        elif "hidden gem" in suggestion:
            added_tip += f"🗺 Don't miss the tucked-away spots in {city}—ask a local or wander aimlessly!"
        elif "adventurous" in suggestion:
            added_tip += f"⛰ Try an outdoor challenge like hiking, biking, or street exploring in {city}!"
        elif "cultural" in suggestion:
            added_tip += f"🎭 Visit a local museum, festival, or take a cultural class!"
        elif "transportation" in suggestion:
            added_tip += f"🚇 Use city cards, bike rentals, or local rideshare apps!"
        elif "safety" in suggestion:
            added_tip += f"🛡 Keep copies of documents, know emergency numbers, trust your instincts!"
        
        return itinerary + added_tip
    
    def create_gradio_interface(self):
        """Create and return Gradio interface"""
        with gr.Blocks(theme="soft", title="Chaotic Compass - Advanced Travel Planner") as demo:
            gr.Markdown(
                """
                # 🚀 **Chaotic Compass - Advanced Edition**
                _Travel Without Rules, Plan With Intelligence!_  
                
                Enter your **city** and **interests** to get a personalized chaotic travel plan with 
                local insights, safety information, and alternative itineraries! 🧭✨
                """
            )
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### 📋 Trip Details")
                    city = gr.Textbox(label="🌍 City", placeholder="e.g., Tokyo, Barcelona, Mumbai")
                    interests = gr.Textbox(label="🎯 Interests", placeholder="e.g., anime, food, temples, nightlife")
                    
                    with gr.Row():
                        budget = gr.Dropdown(
                            choices=["budget", "mid-range", "luxury"], 
                            value="mid-range", 
                            label="💰 Budget"
                        )
                        duration = gr.Dropdown(
                            choices=["1 day", "3 days", "1 week", "2 weeks"], 
                            value="3 days", 
                            label="📅 Duration"
                        )
                    
                    travel_style = gr.Dropdown(
                        choices=["adventurous", "relaxed", "cultural", "party", "family-friendly"],
                        value="adventurous",
                        label="🎒 Travel Style"
                    )
                    
                    submit_btn = gr.Button("🚀 Generate Ultimate Itinerary", variant="primary")
                    
                    gr.Examples(
                        examples=[
                            ["Barcelona", "architecture, beaches, nightlife", "mid-range", "3 days", "adventurous"],
                            ["Seoul", "k-pop, food, shopping", "budget", "1 week", "cultural"],
                            ["Rome", "history, ruins, pizza", "luxury", "1 week", "relaxed"],
                            ["Tokyo", "anime, technology, temples", "mid-range", "2 weeks", "adventurous"],
                        ],
                        inputs=[city, interests, budget, duration, travel_style],
                    )
                
                with gr.Column(scale=2):
                    gr.Markdown("### 📝 Your ChaoticCompass Adventure Plan")
                    output = gr.Markdown(label="✨ Generated Itinerary")
                    
                    follow_btn = gr.Button("💡 Get Additional Suggestion", size="sm")
                    
                    with gr.Accordion("🔄 Alternative Plans", open=False):
                        alt_plans = gr.Markdown("Generate an itinerary to see alternative options!")
                    
                    with gr.Accordion("🗝 Local Insider Tips", open=False):
                        local_tips = gr.Markdown("Generate an itinerary to get local insights!")
                    
                    with gr.Accordion("🛡 Safety & Travel Info", open=False):
                        safety_info = gr.Markdown("Generate an itinerary for safety information!")
                    
                    with gr.Accordion("🕓 Session History", open=False):
                        session_list = gr.Markdown("Your travel planning history will appear here...")

            # Initialize state variables with default values
            itinerary_state = gr.State("")
            city_state = gr.State("")
            interests_state = gr.State("")
            suggestion_state = gr.State("")

            def enhanced_itinerary_generation(city, interests, budget, duration, travel_style):
                if not city or not interests:
                    raise gr.Error("Please enter both city and interests to generate an itinerary")
                
                # Generate main itinerary
                main_itinerary = self.generate_itinerary(city, interests, budget, duration, travel_style)
                result = f"### ✨ Your Chaotic Adventure in {city.title()}\n\n{main_itinerary}"
                
                # Store in session history
                self.session_history.append((city, interests, result))
                
                # Generate additional content
                alt_content = self.generate_alternative_plans(city, interests, duration, travel_style)
                tips_content = self.generate_local_tips(city)
                safety_content = self.generate_safety_info(city)
                
                # Get dynamic suggestion
                suggestion = self.get_dynamic_suggestion(city, interests)
                
                # Create history markdown
                history_md = "\n\n---\n\n".join(
                    [f"**City:** {c}\n**Interests:** {i}\n{r}" for c, i, r in reversed(self.session_history)]
                ) if self.session_history else "No history yet"
                
                return (
                    result,  # main itinerary
                    suggestion,  # follow-up suggestion
                    alt_content,  # alternative plans
                    tips_content,  # local tips
                    safety_content,  # safety info
                    history_md,  # history
                    result,  # itinerary state
                    city,  # city state
                    interests,  # interests state
                    suggestion  # suggestion state
                )

            def handle_suggestion_click(suggestion, itinerary, city, interests):
                if not suggestion:
                    return itinerary
                return self.handle_follow_up(suggestion, itinerary, city, interests)

            # Main submission
            submit_btn.click(
                fn=enhanced_itinerary_generation,
                inputs=[city, interests, budget, duration, travel_style],
                outputs=[
                    output,
                    follow_btn,
                    alt_plans,
                    local_tips,
                    safety_info,
                    session_list,
                    itinerary_state,
                    city_state,
                    interests_state,
                    suggestion_state
                ]
            )

            # Follow-up button
            follow_btn.click(
                fn=handle_suggestion_click,
                inputs=[suggestion_state, itinerary_state, city_state, interests_state],
                outputs=output
            )
        
        return demo