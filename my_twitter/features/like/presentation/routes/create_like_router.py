from fastapi import Depends, Path, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.like.dependencies import get_create_like_use_case
from my_twitter.features.like.domain.use_cases.create_like import CreateLikeUseCase, CreateLikeUseCaseImpl
from my_twitter.features.user.domain.entities.user_entity import UserEntity


router = APIRouter()

@router.post("/{id}/likes")
async def create_like(
        id: int = Path(description="ID твита"),
        current_user: UserEntity = Depends(get_current_user),
        create_like_use_case: CreateLikeUseCaseImpl = Depends(get_create_like_use_case)
):
    await create_like_use_case(id, current_user)
    return {"result": True}
