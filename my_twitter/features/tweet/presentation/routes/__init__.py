from fastapi import APIRouter

router = APIRouter(
    prefix="/api/tweets",
    tags=["tweets"],
)
