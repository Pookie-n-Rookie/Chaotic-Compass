import os
from dotenv import load_dotenv
import gradio as gr
from travel_planner import TravelPlanner
from cli_interface import run_cli_planner

# Load environment variables
load_dotenv()

def main():
    """Main entry point for the application"""
    # print("🚀 Welcome to Chaotic Compass Advanced Travel Planner!")
    # print("Choose your adventure:")
    # print("1. Interactive CLI Planner (Full Workflow)")
    # print("2. Quick Web Interface")
    
    # choice = input("Enter your choice (1/2): ").strip()
    
    # if choice == "1":
    #     run_cli_planner()
    # else:
        # Launch Gradio interface
    planner = TravelPlanner()
    demo = planner.create_gradio_interface()
    demo.launch(share=True)

if __name__ == "__main__":
    main()