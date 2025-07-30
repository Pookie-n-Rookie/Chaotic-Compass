# 🚀 Chaotic Compass - Advanced Travel Planner

**Travel Without Rules, Plan With Intelligence!**

A revolutionary AI-powered travel planning application that creates chaotic, exciting, and personalized travel itineraries using LangChain, LangGraph, and Groq AI. Whether you're seeking adventure, culture, relaxation, or pure chaos, Chaotic Compass has got you covered!

## ✨ Features

- **🎯 Personalized Itineraries**: AI-generated travel plans based on your interests, budget, and travel style
- **🔄 Alternative Plans**: Multiple itinerary options including budget-focused, luxury, and off-the-beaten-path alternatives  
- **🗝️ Local Insider Tips**: Hidden gems and cultural insights from locals
- **🛡️ Safety Information**: Comprehensive safety guidelines and travel advisories
- **💡 Dynamic Suggestions**: Interactive follow-up recommendations to enhance your trip
- **🖥️ Dual Interface**: Choose between CLI workflow or modern web interface
- **📊 Session History**: Track your travel planning journey

## 🏗️ Architecture

The application uses a sophisticated **LangGraph workflow** with multiple AI-powered nodes:

```
Input Collection → Itinerary Generation → Recommendations → 
Local Tips → Safety Info → Alternative Plans → Satisfaction Check → 
Refinement Loop → Final Plan
```

### Key Components:

- **State Management**: TypedDict-based state tracking across the workflow
- **AI Integration**: Groq's Llama-3.3-70B model for intelligent content generation
- **Workflow Engine**: LangGraph for complex multi-step planning processes
- **Web Interface**: Modern Gradio-based UI with interactive elements
- **CLI Interface**: Command-line workflow for detailed step-by-step planning

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chaotic-compass.git
   cd chaotic-compass
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 💻 Usage

### Web Interface (Recommended)
- Choose option `2` when prompted
- Fill in your travel preferences in the intuitive web form
- Get instant AI-generated itineraries with additional insights
- Use the dynamic suggestion button for follow-up recommendations

### CLI Interface (Advanced)
- Choose option `1` for the full interactive workflow
- Follow step-by-step prompts for detailed travel planning
- Get comprehensive plans with refinement capabilities
- Perfect for users who want maximum customization

## 📁 Project Structure

```
chaotic-compass/
├── main.py                 # Application entry point
├── travel_planner.py       # Main TravelPlanner class with Gradio interface
├── state_definitions.py    # TypedDict state definitions
├── workflow_nodes.py       # LangGraph node functions
├── workflow_engine.py      # Workflow compilation and routing
├── cli_interface.py        # CLI interface functions
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🛠️ Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Customization Options

**Travel Styles**:
- `adventurous` - High-energy, extreme activities
- `relaxed` - Peaceful, leisure-focused
- `cultural` - Museums, local traditions, arts
- `party` - Nightlife, social events
- `family-friendly` - Kid-safe activities

**Budget Ranges**:
- `budget` - Cost-effective options
- `mid-range` - Balanced comfort and cost
- `luxury` - Premium experiences

**Duration Options**:
- `1 day` - Quick city exploration
- `3 days` - Weekend getaway
- `1 week` - Comprehensive vacation
- `2 weeks` - Extended adventure

## 🎯 Example Usage

```python
# Quick example using the TravelPlanner class
from travel_planner import TravelPlanner

planner = TravelPlanner()
itinerary = planner.generate_itinerary(
    city="Tokyo",
    interests="anime, food, temples",
    budget="mid-range",
    duration="1 week",
    travel_style="adventurous"
)
print(itinerary)
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (when available)
python -m pytest

# Format code
black .
```

## 📋 Roadmap

- [ ] **Multi-language Support** - Support for multiple languages
- [ ] **Real-time Weather Integration** - Live weather data
- [ ] **Social Media Integration** - Share itineraries easily  
- [ ] **Mobile App** - Native mobile applications
- [ ] **Booking Integration** - Direct hotel/flight booking
- [ ] **Community Features** - User reviews and ratings
- [ ] **Offline Mode** - Downloaded itineraries for offline use

## 🔧 Troubleshooting

### Common Issues

1. **GROQ_API_KEY not found**
   - Ensure your `.env` file contains `GROQ_API_KEY=your_actual_key`
   - Restart the application after adding the key

2. **Import errors**
   - Run `pip install -r requirements.txt` to install all dependencies
   - Check Python version (3.8+ required)

3. **Gradio interface not loading**
   - Check if port 7860 is available
   - Try running with `demo.launch(server_port=8080)` for different port

### Performance Tips

- Use shorter interest lists for faster generation
- Choose `1 day` or `3 days` for quicker responses
- The CLI interface provides more detailed outputs but takes longer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the awesome AI framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) for workflow orchestration
- [Groq](https://groq.com/) for lightning-fast AI inference
- [Gradio](https://gradio.app/) for the beautiful web interface




**Built with ❤️ by Swarnendu Banerjee**

*Ready to embark on your next chaotic adventure? Let's go! 🧭✨*
