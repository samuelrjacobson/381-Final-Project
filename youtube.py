from config import YOUTUBE_API_KEY, CLOUD_TRANSLATION_API_KEY
from googleapiclient.discovery import build

YOUTUBE_DEVELOPER_KEY = YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=YOUTUBE_DEVELOPER_KEY)
translator = build(
        "translate", "v2", developerKey=CLOUD_TRANSLATION_API_KEY)

def reviews_search(movie_name):

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

def get_full_description(video_id):
    
    video = youtube.videos().list(
        id=video_id,
        part='snippet',
    ).execute()

    return video['items'][0]['snippet']['description']

def other_language(lang, movie_title):

    translated_query = translator.translations().list(source="en", target=lang, q=[f"{movie_title} movie review commentary"]).execute()

    translated_query = translated_query['translations'][0]['translatedText']

    search_response = youtube.search().list(
        part='id,snippet',
        q=translated_query,
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
