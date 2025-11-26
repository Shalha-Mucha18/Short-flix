from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_SHORTS = [
    {"id": 1, "videoUrl": "https://www.w3schools.com/html/mov_bbb.mp4", "title": "Travel Reel", "tags": ["adventure", "outdoors", "cinematic"]},
    {"id": 2, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4", "title": "City Pulse", "tags": ["city", "nightlife", "lights"]},
    {"id": 3, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4", "title": "Calm Shores", "tags": ["ocean", "drone", "relax"]},
    {"id": 4, "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4", "title": "Hike Time", "tags": ["mountains", "trail", "nature"]},
]

class ShortCreate(BaseModel):
    videoUrl: str
    title: str
    tags: List[str]

@app.get("/")
def get_shorts():
    return _SHORTS

@app.post("/")
def create_short(short: ShortCreate):
    if not short.tags:
        raise HTTPException(400, "At least one tag is required.")
    next_id = max((item['id'] for item in _SHORTS), default=0) + 1
    new_short = {"id": next_id, "videoUrl": short.videoUrl, "title": short.title, "tags": short.tags}
    _SHORTS.append(new_short)
    return new_short

@app.delete("/{short_id}")
def delete_short(short_id: int):
    for i, s in enumerate(_SHORTS):
        if s['id'] == short_id:
            _SHORTS.pop(i)
            return {"status": "deleted"}
    raise HTTPException(404, "Short not found")

handler = app
