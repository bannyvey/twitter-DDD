from fastapi import APIRouter

from .create_tweet_router import router as create_router
from . delete_tweet_router import router as delete_router
from .get_tweets_router import router as get_router


router = APIRouter(
    prefix="/api/tweets",
    tags=["tweets"],
)

router.include_router(create_router)
router.include_router(delete_router)
router.include_router(get_router)