from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from backend.app.schemas.short import Short, ShortCreate
from backend.app.services.short_service import create_short, delete_short, list_shorts

router = APIRouter(tags=["shorts"])


@router.get("", response_model=List[Short])
def get_shorts(
    q: Optional[str] = Query(None, description="search by title or tag"),
    tag: Optional[str] = Query(None, description="filter by tag"),
) -> List[Short]:
    return list_shorts(q=q, tag=tag)


@router.post("", response_model=Short, status_code=status.HTTP_201_CREATED)
def add_short(payload: ShortCreate) -> Short:
    if not payload.tags:
        raise HTTPException(status_code=400, detail="Tags are required.")
    return create_short(payload)


@router.delete("/{short_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_short(short_id: int) -> None:
    deleted = delete_short(short_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Short not found")
