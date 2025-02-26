import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize AI Model
llm = ChatGroq(
    temperature=0,
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

# Itinerary Prompt
itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are ChaoticCompass, a wild and unpredictable travel assistant. "
               "Introduce yourself with flair, then create a crazy, fun day trip itinerary "
               "for {city} based on {interests}. Keep it brief, exciting, and unique!"),
    ("human", "Create an itinerary for my day trip."),
])

def generate_itinerary(city: str, interests: str):
    """Generates a chaotic and fun travel itinerary."""
    response = llm.invoke(itinerary_prompt.format_messages(city=city, interests=interests))
    return response.content
