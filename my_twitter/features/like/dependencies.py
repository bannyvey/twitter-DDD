from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.core.database.postgres.database import get_db
from my_twitter.features.like.data.repositories.like_repository_impl import LikeRepositoryImpl
from my_twitter.features.like.data.repositories.like_unit_of_work_impl import LikeUnitOfWorkImpl
from my_twitter.features.like.domain.repositories.like_repository import LikeRepository
from my_twitter.features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork
from my_twitter.features.like.domain.use_cases.create_like import CreateLikeUseCase, CreateLikeUseCaseImpl
from my_twitter.features.like.domain.use_cases.delete_like import DeleteLikeUseCase, DeleteLikeUseCaseImpl


def get_like_repository(
        session: AsyncSession = Depends(get_db)
):
    return LikeRepositoryImpl(session)


def get_like_unit_of_work(
        session: AsyncSession = Depends(get_db),
        repository: LikeRepositoryImpl = Depends(get_like_repository)
):
    return LikeUnitOfWorkImpl(session, repository)


def get_delete_like_use_case(
        like_unit_of_work: LikeUnitOfWorkImpl = Depends(get_like_unit_of_work)
) -> DeleteLikeUseCase:
    return DeleteLikeUseCaseImpl(like_unit_of_work)


def get_create_like_use_case(
        like_unit_of_work: LikeUnitOfWorkImpl = Depends(get_like_unit_of_work)
) -> CreateLikeUseCase:
    return CreateLikeUseCaseImpl(like_unit_of_work)
