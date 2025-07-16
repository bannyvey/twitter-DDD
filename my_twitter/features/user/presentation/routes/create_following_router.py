from fastapi import Depends

from dependencies import get_current_user
from features.user.dependencies import get_create_following_use_case
from features.user.domain.entities.user_entity import UserEntity
from features.user.domain.use_cases.create_follower import CreateFollowerUseCase
from features.user.presentation.routes import router


@router.post("/{id}/follow")
async def create_following(
        id: int,
        current_user: UserEntity = Depends(get_current_user),
        create_following_use_case: CreateFollowerUseCase = Depends(get_create_following_use_case)
):
    await create_following_use_case(current_user, id)
    return {"result": True}

