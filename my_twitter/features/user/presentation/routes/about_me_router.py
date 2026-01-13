from fastapi import Depends, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.user.dependencies import get_tweet_me_use_case
from my_twitter.features.user.domain.entities.user_entity import UserEntity
from my_twitter.features.user.domain.use_cases.get_me_user import UserGetMeUseCase

router = APIRouter()

@router.get('/me')
async def about_me_router(
        current_user: UserEntity = Depends(get_current_user),
        about_me_use_case: UserGetMeUseCase = Depends(get_tweet_me_use_case)
):
    result = await about_me_use_case()
    return result
