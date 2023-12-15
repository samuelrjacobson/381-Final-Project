import config
from googleapiclient.discovery import build

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def reviews_search(movie_name):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        part='id,snippet',
        q=f"{movie_name} movie review commentary",
        type='video',
        maxResults=10,
        order='relevance',
    ).execute()

    reviews_list = []
    for item in search_response.get('items', []):
        id = item['id']['videoId']
        title = item['snippet']['title']
        description = item['snippet']['description']

        reviews_list.append({
            'id': id,
            'title': title,
            'description': description
        })

    return reviews_list
