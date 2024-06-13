import os
import pprint
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain_community.utilities import GoogleSerperAPIWrapper

# Load environment variables from .env file
load_dotenv()

# Load API Key
api_key = os.getenv('SERPER_API_KEY')

# Query
query = "rramos github tech and data notes"

search = GoogleSerperAPIWrapper()
res = search.run(query)

pprint.pp(res)

