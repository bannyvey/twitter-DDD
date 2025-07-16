from fastapi import Depends, Path

from dependencies import get_current_user
from features.like.dependencies import get_delete_like_use_case
from features.like.domain.use_cases.delete_like import DeleteLikeUseCase
from features.like.presentation import router
from features.user.domain.entities.user_entity import UserEntity


@router.delete("/{id}/likes")
async def delete_like(
        id: int = Path(description="ID твита"),
        delete_like_use_case: DeleteLikeUseCase = Depends(get_delete_like_use_case),
        current_user: UserEntity = Depends(get_current_user)
):
    await delete_like_use_case(id, current_user)
    return {"result": True}
