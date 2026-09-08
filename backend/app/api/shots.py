from typing import Annotated

from fastapi import APIRouter, Query

from app import search

router = APIRouter()


@router.get("/shots")
def shots(ids: Annotated[list[str], Query()] = []) -> list[dict]:  # noqa: B006
    return search.get_shots(ids)


@router.get("/shots/{shot_id}/similar")
def similar(shot_id: str, limit: int = 24) -> list[dict]:
    return search.similar_shots(shot_id, limit)
