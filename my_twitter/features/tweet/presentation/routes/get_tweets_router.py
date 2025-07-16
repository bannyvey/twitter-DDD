from fastapi import Depends

from dependencies import get_current_user
from features.tweet.dependencies import get_tweet_use_case
from features.tweet.domain.entities.tweet_common_model import AllTweetsResponseScheme
from features.tweet.domain.use_cases.get_tweets import GetTweetsUseCase
from features.tweet.presentation.routes import router
from features.user.data.models.user import User


@router.get("/", response_model=AllTweetsResponseScheme)
async def get_tweets(
        get_tweets_use_case: GetTweetsUseCase = Depends(get_tweet_use_case),
        current_user: User = Depends(get_current_user)
):
    all_tweets = await get_tweets_use_case()
    return AllTweetsResponseScheme(tweets=all_tweets)
