from fastapi import Depends, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.user.dependencies import get_create_following_use_case
from my_twitter.features.user.domain.entities.user_entity import UserEntity
from my_twitter.features.user.domain.use_cases.create_follower import CreateFollowerUseCase

router = APIRouter()

@router.post("/{id}/follow")
async def create_following(
        id: int,
        current_user: UserEntity = Depends(get_current_user),
        create_following_use_case: CreateFollowerUseCase = Depends(get_create_following_use_case)
):
    await create_following_use_case(current_user, id)
    return {"result": True}

