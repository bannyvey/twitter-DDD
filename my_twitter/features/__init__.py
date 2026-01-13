from fastapi import APIRouter

from .auth.presentation import router as auth_router
from .like.presentation import router as like_router
from .tweet.presentation import router as tweet_router
from .media.presentation import router as media_router
from .user.presentation import router as user_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(like_router)
router.include_router(tweet_router)
router.include_router(media_router)
router.include_router(user_router)


