from fastapi import Depends, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.tweet.dependencies import get_create_tweet_use_case
from my_twitter.features.tweet.domain.entities.tweet_command_model import TweetCreateModel
from my_twitter.features.tweet.domain.use_cases.create_tweet import CreateTweetUseCase
from my_twitter.features.tweet.presentation.schemas.tweet_schema import TweetResponseSchema
from my_twitter.features.user.domain.entities.user_entity import UserEntity

router = APIRouter()

@router.post('/', response_model=TweetResponseSchema)
async def create_tweet(
        data: TweetCreateModel,
        current_user: UserEntity = Depends(get_current_user),
        create_tweet_use_case: CreateTweetUseCase = Depends(get_create_tweet_use_case)
):
    tweet = await create_tweet_use_case(data, current_user)

    return {"result": True, "tweet_id": tweet.id_}
