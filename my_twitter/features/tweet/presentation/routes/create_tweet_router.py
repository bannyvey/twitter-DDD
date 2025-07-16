from fastapi import Depends

from dependencies import get_current_user
from features.tweet.dependencies import get_create_tweet_use_case
from features.tweet.domain.entities.tweet_command_model import TweetCreateModel
from features.tweet.domain.use_cases.create_tweet import CreateTweetUseCase
from features.tweet.presentation.routes import router
from features.tweet.presentation.schemas.tweet_schema import TweetResponseSchema
from features.user.domain.entities.user_entity import UserEntity


@router.post('/', response_model=TweetResponseSchema)
async def create_tweet(
        data: TweetCreateModel,
        current_user: UserEntity = Depends(get_current_user),
        create_tweet_use_case: CreateTweetUseCase = Depends(get_create_tweet_use_case)
):
    tweet = await create_tweet_use_case(data, current_user)

    return {"result": True, "tweet_id": tweet.id_}
