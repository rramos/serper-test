import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from langchain_community.llms import Ollama

# Load environment variables from .env file
load_dotenv()

# Load API Key
api_key = os.getenv('SERPER_API_KEY')

# Query
query="rramos github tech and data notes"

llm = Ollama(temperature=0,model="llama3")
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run(query),
        description="useful for when you need to ask with search",
    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
)
self_ask_with_search.invoke(
    "resume the search results ?"
)

