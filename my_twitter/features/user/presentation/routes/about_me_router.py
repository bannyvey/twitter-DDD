from fastapi import Depends

from dependencies import get_current_user
from features.user.dependencies import get_tweet_me_use_case
from features.user.domain.entities.user_entity import UserEntity
from features.user.domain.use_cases.get_me_user import UserGetMeUseCase
from features.user.presentation.routes import router


@router.get('/me')
async def about_me_router(
        current_user: UserEntity = Depends(get_current_user),
        about_me_use_case: UserGetMeUseCase = Depends(get_tweet_me_use_case)
):
    result = await about_me_use_case()
    return result
