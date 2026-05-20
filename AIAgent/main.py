import os

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

# 1. Properly decorate your tool so Gemini understands the arguments
@tool
def get_weather(city: str) -> str:
    """Get weather conditions for a given city."""
    # LLM tools should ideally return a string or stringified JSON
    return f"The weather in {city} is sunny and 25 degrees."

@tool
def get_location():
    """Get users current location."""
    return "Rome,Italy"

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-3.5-flash",
   temperature=0.7
)

system_prompt="""
You are a helpful weather assistant.
YOUR WORKFLOW:
1. If the user asks about weather WITHOUT specyfing a location you must
- call get_location to find the city
- call get_weather with that location
2. I the user provides a city, call get_weather with that city
"""

agent = create_agent(
    model=llm,
    tools=[get_weather,get_location],
    system_prompt=system_prompt
)

user_query = input("Enter your query: ")

response1 = agent.invoke(
    {"messages":
         [
             {'role':'user','content':user_query},
         ]
    })

# response1 = llm.invoke('How is the weather in Rome')
print(response1['messages'][-1].content)
