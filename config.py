import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    TOKEN = os.getenv("TOKEN")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    # ....
