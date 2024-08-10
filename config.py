import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    # more below...