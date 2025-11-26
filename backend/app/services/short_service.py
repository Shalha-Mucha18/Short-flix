from typing import List, Optional

from backend.app.schemas.short import Short, ShortCreate

_SHORTS: List[dict] = [
    {
        "id": 1,
        "videoUrl": "https://www.w3schools.com/html/mov_bbb.mp4",
        "title": "Travel Reel",
        "tags": ["adventure", "outdoors", "cinematic"],
    },
    {
        "id": 2,
        "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4",
        "title": "City Pulse",
        "tags": ["city", "nightlife", "lights"],
    },
    {
        "id": 3,
        "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4",
        "title": "Calm Shores",
        "tags": ["ocean", "drone", "relax"],
    },
    {
        "id": 4,
        "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4",
        "title": "Hike Time",
        "tags": ["mountains", "trail", "nature"],
    },
]


def list_shorts(q: Optional[str] = None, tag: Optional[str] = None) -> List[Short]:
    items = _SHORTS

    if q:
        query = q.lower()
        items = [
            item
            for item in items
            if query in item["title"].lower()
            or any(query in t.lower() for t in item["tags"])
        ]

    if tag:
        tag_lower = tag.lower()
        items = [
            item for item in items if any(tag_lower == t.lower() for t in item["tags"])
        ]

    return [Short(**item) for item in items]


def create_short(payload: ShortCreate) -> Short:
    next_id = max((item["id"] for item in _SHORTS), default=0) + 1
    record = Short(id=next_id, **payload.model_dump())
    _SHORTS.append(record.model_dump())
    return record


def delete_short(short_id: int) -> bool:
    """Remove a short by id; returns True if removed."""
    index = next((i for i, item in enumerate(_SHORTS) if item["id"] == short_id), None)
    if index is None:
        return False
    _SHORTS.pop(index)
    return True
