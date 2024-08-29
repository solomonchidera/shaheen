import os
from googleapiclient.discovery import build

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_youtube_service():
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetch_random_video(topic="technology", max_results=10):
    youtube = get_youtube_service()
    search_response = youtube.search().list(
        q=topic,
        part='snippet',
        maxResults=max_results,
        type='video',
        order='relevance'
    ).execute()

    videos = search_response.get('items', [])
    return videos
