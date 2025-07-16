from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.postgres.database import get_db
from features.like.data.repositories.like_repository_impl import LikeRepositoryImpl
from features.like.data.repositories.like_unit_of_work_impl import LikeUnitOfWorkImpl
from features.like.domain.repositories.like_repository import LikeRepository
from features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork
from features.like.domain.use_cases.create_like import CreateLikeUseCase, CreateLikeUseCaseImpl
from features.like.domain.use_cases.delete_like import DeleteLikeUseCase, DeleteLikeUseCaseImpl


def get_like_repository(
        session: AsyncSession = Depends(get_db)
):
    return LikeRepositoryImpl(session)


def get_like_unit_of_work(
        session: AsyncSession = Depends(get_db),
        repository: LikeRepository = Depends(get_like_repository)
):
    return LikeUnitOfWorkImpl(session, repository)


def get_delete_like_use_case(
        like_unit_of_work: LikeUnitOfWork = Depends(get_like_unit_of_work)
) -> DeleteLikeUseCase:
    return DeleteLikeUseCaseImpl(like_unit_of_work)


def get_create_like_use_case(
        like_unit_of_work: LikeUnitOfWork = Depends(get_like_unit_of_work)
) -> CreateLikeUseCase:
    return CreateLikeUseCaseImpl(like_unit_of_work)
