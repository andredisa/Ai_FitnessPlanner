from agno.agent import Agent
from agno.models.google import Gemini

def create_agents(api_key):
    gemini_model = Gemini(id="gemini-1.5-flash", api_key=api_key)
    
    dietary_agent = Agent(
        name="Dietary Expert",
        role="Provides personalized dietary recommendations",
        model=gemini_model,
        instructions=[
            "Consider the user's input, including dietary restrictions and preferences.",
            "Suggest a detailed meal plan for the day, including breakfast, lunch, dinner, and snacks.",
            "Provide a brief explanation of why the plan is suited to the user's goals.",
            "Focus on clarity, coherence, and quality of the recommendations.",
        ]
    )

    fitness_agent = Agent(
        name="Fitness Expert",
        role="Provides personalized fitness recommendations",
        model=gemini_model,
        instructions=[
            "Provide exercises tailored to the user's goals.",
            "Include warm-up, main workout, and cool-down exercises.",
            "Explain the benefits of each recommended exercise.",
            "Ensure the plan is actionable and detailed.",
        ]
    )

    return dietary_agent, fitness_agent
