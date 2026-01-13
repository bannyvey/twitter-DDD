from fastapi import Depends, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.tweet.dependencies import get_tweet_use_case
from my_twitter.features.tweet.domain.entities.tweet_common_model import AllTweetsResponseScheme
from my_twitter.features.tweet.domain.use_cases.get_tweets import GetTweetsUseCase
from my_twitter.features.user.domain.entities.user_entity import UserEntity

router = APIRouter()

@router.get("/", response_model=AllTweetsResponseScheme)
async def get_tweets(
        get_tweets_use_case: GetTweetsUseCase = Depends(get_tweet_use_case),
        current_user: UserEntity = Depends(get_current_user)
):
    all_tweets = await get_tweets_use_case()
    return AllTweetsResponseScheme(tweets=all_tweets)
