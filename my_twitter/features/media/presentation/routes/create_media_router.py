from fastapi import UploadFile, Depends

from dependencies import get_current_user
from features.media.dependencies import get_create_media_use_case
from features.media.domain.use_cases.create_media import CreateMediaUseCase
from features.media.presentation.routes import router
from features.user.domain.entities.user_entity import UserEntity


@router.post("/")
async def create_media(
        path: UploadFile | None = None,
        current_user: UserEntity | None = Depends(get_current_user),
        create_media_use_case: CreateMediaUseCase = Depends(get_create_media_use_case)
):
    media = await create_media_use_case(path)
    return {"result": True, "media_id": media.id_}
