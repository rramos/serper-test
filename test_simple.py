import requests
import json
import os
from dotenv import load_dotenv

url = "https://google.serper.dev/search"

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('SERPER_API_KEY')

# Search query
query = "apple inc"

payload = json.dumps({
  "q": query
})
headers = {
  'X-API-KEY': api_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)