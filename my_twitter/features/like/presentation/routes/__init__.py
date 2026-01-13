from fastapi import APIRouter

from .create_like_router import router as create_like
from .delete_like_router import router as delete_like

router = APIRouter(
    prefix="/api/tweets",
    tags=["likes"]
)

router.include_router(create_like)
router.include_router(delete_like)