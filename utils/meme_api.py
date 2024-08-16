"""defines a function make a request to the memes API and reatruns a meme"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def get_meme():
    """Make an api request to programming memes rapidapi

    Returns:
        str: link of a meme
    """

    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "programming-memes-images.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        image = data[0]['image']
        return image
    else:
        return