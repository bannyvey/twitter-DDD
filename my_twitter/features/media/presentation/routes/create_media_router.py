from fastapi import UploadFile, Depends, APIRouter

from my_twitter.dependencies import get_current_user
from my_twitter.features.media.dependencies import get_create_media_use_case
from my_twitter.features.media.domain.use_cases.create_media import CreateMediaUseCase
from my_twitter.features.user.domain.entities.user_entity import UserEntity

router = APIRouter()

@router.post("/")
async def create_media(
        path: UploadFile | None = None,
        current_user: UserEntity | None = Depends(get_current_user),
        create_media_use_case: CreateMediaUseCase = Depends(get_create_media_use_case)
):
    media = await create_media_use_case(path)
    return {"result": True, "media_id": media.id_}
