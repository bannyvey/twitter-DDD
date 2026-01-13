from fastapi import Depends, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from my_twitter.core.database.postgres.database import get_db
from my_twitter.features.media.data.repositories.media_repository_impl import MediaRepositoryImpl
from my_twitter.features.media.data.repositories.media_unit_of_work_impl import MediaUnitOfWorkImpl
from my_twitter.features.media.domain.repositories.media_repository import MediaRepository
from my_twitter.features.media.domain.repositories.media_unit_of_work import MediaUnitOfWork
from my_twitter.features.media.domain.use_cases.create_media import CreateMediaUseCase, CreateMediaUseCaseImpl


def get_media_repository(
        session: AsyncSession = Depends(get_db),
) -> MediaRepository:
    return MediaRepositoryImpl(session)


def get_media_unit_of_work(
        session: AsyncSession = Depends(get_db),
        tweet_repository: MediaRepository = Depends(get_media_repository),
) -> MediaUnitOfWork:
    return MediaUnitOfWorkImpl(session, tweet_repository)


def get_create_media_use_case(
        media_unit_of_work: MediaUnitOfWork = Depends(get_media_unit_of_work)
) -> CreateMediaUseCase:
    return CreateMediaUseCaseImpl(media_unit_of_work)
