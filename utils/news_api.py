import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_articles(topic=None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": NEWS_API_KEY,
        "category": "technology",
        "pageSize": 10,
        "language": "en"
    }
    if topic:
        params["q"] = topic

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        return []