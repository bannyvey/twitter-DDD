from fastapi import APIRouter

from .create_media_router import router as create_router

router = APIRouter(
    prefix="/api/medias",
    tags=["media"],
)

router.include_router(create_router)
