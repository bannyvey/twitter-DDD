import os

import aiofiles
from fastapi import UploadFile

from config import PATH_MEDIA
from core.error.media_exception import MediaNotFound
from core.use_case.use_case import BaseUseCase
from features.media.domain.entities.media_entity import MediaEntity
from features.media.domain.repositories.media_unit_of_work import MediaUnitOfWork


class CreateMediaUseCase(BaseUseCase[MediaEntity, None]):
    unit_of_work: MediaUnitOfWork

    async def __call__(self, file: UploadFile | None = None) -> MediaEntity:
        raise NotImplementedError()


class CreateMediaUseCaseImpl(CreateMediaUseCase):
    def __init__(self, unit_of_work: MediaUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, file: UploadFile | None = None) -> MediaEntity:
        if not file or not file.filename:
            raise MediaNotFound

        os.makedirs(PATH_MEDIA, exist_ok=True)
        file_path = os.path.join(PATH_MEDIA, file.filename)
        async with aiofiles.open(file_path, "wb") as f:
            content = await file.read()
            await f.write(content)
        media_ = MediaEntity(
            id_=None,
            path=file_path
        )
        try:
            result = await self.unit_of_work.repository.create(media_)
        except Exception as e:
            await self.unit_of_work.rollback()
            raise e

        await self.unit_of_work.commit()
        return result




