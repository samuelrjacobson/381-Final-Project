from fastapi import FastAPI, HTTPException
from youtube import reviews_search, get_full_description
from typing import List

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"status": "Hello, world"}

@app.get("/moviereviews/{movie_name}", response_model=List[dict])
async def get_video_list(movie_name: str):
    try:
        return reviews_search(movie_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/descriptions/{video_id}")
async def get_description(video_id: str):
    try:
        return get_full_description(video_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))