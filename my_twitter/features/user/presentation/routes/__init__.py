from fastapi import APIRouter

from .about_me_router import router as about_router
from .create_following_router import router as create_router
from .delete_following_router import router as delete_user
from .find_by_id_router import router as find_router

router = APIRouter(
    prefix="/api/users",
    tags=["users"]
)

router.include_router(about_router)
router.include_router(create_router)
router.include_router(delete_user)
router.include_router(find_router)

