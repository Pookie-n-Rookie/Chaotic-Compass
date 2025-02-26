import gradio as gr
from itinerary import generate_itinerary  # Import itinerary generator

# Define Gradio Interface
interface = gr.Interface(
    fn=generate_itinerary,
    inputs=[
        gr.Textbox(label="Enter the city for your chaotic adventure"),
        gr.Textbox(label="Enter your interests (comma-separated)"),
    ],
    outputs=gr.Textbox(label="Your ChaoticCompass Itinerary"),
    title="🚀 Chaotic Compass - Travel Without Rules!",
    description="Welcome to ChaoticCompass! I create **crazy, unexpected, and fun travel plans**. Just enter your city and interests, and I'll handle the rest! 😎",
    theme="d8ahazard/material_design_rd",  
)

# Launch Gradio App
if __name__ == "__main__":
    interface.launch(share=True)  # Allows public access
