from .login_router import router as login_router
from .register_router import router as register_router

from fastapi import APIRouter


router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)


router.include_router(login_router)
router.include_router(register_router)