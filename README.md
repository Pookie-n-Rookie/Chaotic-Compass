
# 🚀 Chaotic Compass - AI Multiagent Travel Planner 🌍

Welcome to **Chaotic Compass**, the most **unpredictable, AI-powered travel assistant**!  
Forget boring itineraries – this app creates **chaotic, fun, and unique** travel plans based on your **city** and **wild interests**.  



## 🤖 AI Multiagent System with Langraph

Chaotic Compass is built using **Langraph**, leveraging **state graphs** to define travel planning workflows.  
It intelligently processes user input and dynamically **constructs** an itinerary using **AI agents**.  

## 🔑 Key Components

- **StateGraph** 🕸️ - Defines the workflow of the Travel Planner.
- **PlannerState** 📌 - A structured state representation of the planning process.
- **Node Functions** 🔄 - Individual steps in the planning flow:
  - `input_city` - Captures the city name.
  - `input_interests` - Extracts user interests.
  - `create_itinerary` - Generates a **wild** travel plan.
- **LLM Integration** 🧠 - Uses **Groq-powered AI** to generate personalized itineraries.
- **Multiagent Collaboration** 🤝 - Handles **multiple decision-making agents** for better itinerary generation.


# 🎯 How It Works
1. **User Input** 🎤 - Enter your **city** and **interests**.
2. **StateGraph Activation** ⚙️ - Langraph processes inputs through **planner nodes**.
3. **LLM Processing** 💡 - The AI **constructs** a crazy, unpredictable itinerary.
4. **Response Generation** 📜 - The travel plan is displayed via **Gradio UI**.

## Graph Visualization
 ![image](https://github.com/user-attachments/assets/3130911f-35e4-4f00-924e-3b567b1bbeb7)

## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Pookie-n-Rookie/Chaotic-Compass.git
cd Chaotic-Compass
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a **.env** file and set your **Groq API key**:

```bash
GROQ_API_KEY=your_api_key_here" 
```
## 🚀 Running Chaotic Compass

Launch the **Gradio UI**:
```bash
cd app
python main.py
```

You'll see a local link. Open it in your browser and start **your chaotic adventure!** 🎢

## 📡 Future Enhancements

- 🌍 **Real-time Location API** for up-to-date travel suggestions.
- 🤖 **Autonomous AI Agents** to refine recommendations.
- 📊 **User Preference Learning** for **personalized chaos**.



