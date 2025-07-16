from fastapi import Depends, Path

from dependencies import get_current_user
from features.like.dependencies import get_create_like_use_case
from features.like.domain.use_cases.create_like import CreateLikeUseCase
from features.like.presentation import router
from features.user.domain.entities.user_entity import UserEntity


@router.post("/{id}/likes")
async def create_like(
        id: int = Path(description="ID твита"),
        current_user: UserEntity = Depends(get_current_user),
        create_like_use_case: CreateLikeUseCase = Depends(get_create_like_use_case)
):
    await create_like_use_case(id, current_user)
    return {"result": True}
