# Import the Agent class from Google's ADK (Agent Development Kit)
from google.adk.agents import Agent

# root_agent is the main entry point that ADK looks for when running the agent
# This instance defines the agent's behavior and configuration
root_agent = Agent(
    # Unique identifier for the agent
    name="welcome_agent",
    
    # Specifies which LLM model to use (Gemini 2.0 Flash in this case)
    # Available models: https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    
    # Brief description of the agent's purpose
    description="Greeting agent",
    
    # Instructions that define the agent's behavior and personality
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)