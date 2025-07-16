from fastapi import Depends

from dependencies import get_current_user
from features.user.dependencies import get_delete_following_use_case
from features.user.domain.entities.user_entity import UserEntity
from features.user.domain.use_cases.delete_follower import DeleteFollowingUseCase
from features.user.presentation.routes import router


@router.delete("/{id}/follow")
async def delete_following(
        id: int,
        current_user: UserEntity = Depends(get_current_user),
        delete_following_use_case: DeleteFollowingUseCase = Depends(get_delete_following_use_case)
):
    await delete_following_use_case(current_user, id)
    return {"result": True}
