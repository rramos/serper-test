import requests
import json
import os
from dotenv import load_dotenv

url = "https://google.serper.dev/search"

# Load environment variables from .env file
load_dotenv()

# Load API Key
api_key = os.getenv('SERPER_API_KEY')

search = GoogleSerperAPIWrapper()
search.run("Obama's first name?")



