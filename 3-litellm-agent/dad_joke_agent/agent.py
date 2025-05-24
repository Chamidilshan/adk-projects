import os
import random
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def get_dad_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I would tell you a joke about construction, but I'm still working on it.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    return random.choice(jokes)

model = LiteLlm(
    model="nvidia_nim/meta/llama3-70b-instruct",
    api_key = os.getenv("NVIDIA_API_KEY"),
    drop_params=True,
)

root_agent = Agent(
    name='dad_joke_agent',
    model=model,
    description='Dad joke agent',
    instruction="""
You are a helpful assistant that can tell dad jokes. Only use the tool `get_dad_joke` to tell jokes.""",
    tools=[get_dad_joke]
)
