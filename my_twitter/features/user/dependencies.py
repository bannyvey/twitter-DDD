from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.core.database.postgres.database import get_db
from my_twitter.features.user.data.repositories.user_repository_impl import UserRepositoryImpl
from my_twitter.features.user.data.repositories.user_unit_of_work_impl import UserUnitOfWorkImpl
from my_twitter.features.user.data.services.user_query_service_impl import UserQueryServiceImpl
from my_twitter.features.user.domain.repositories.user_repository import UserRepository
from my_twitter.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork
from my_twitter.features.user.domain.services.user_query_service import UserQueryService
from my_twitter.features.user.domain.use_cases.create_follower import CreateFollowerUseCase, CreateFollowerUseCaseImpl
from my_twitter.features.user.domain.use_cases.delete_follower import DeleteFollowingUseCaseImpl, DeleteFollowingUseCase
from my_twitter.features.user.domain.use_cases.find_by_id_user import FindByIdUserUseCase, FindByIdUserUseCaseImpl
from my_twitter.features.user.domain.use_cases.get_me_user import UserGetMeUseCase, UserGetMeUseCaseImpl


def get_user_repository(
        session: AsyncSession = Depends(get_db),
) -> UserRepository:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
        session: AsyncSession = Depends(get_db),
        user_repository: UserRepository = Depends(get_user_repository)
) -> UserUnitOfWork:
    return UserUnitOfWorkImpl(session, user_repository)


def get_user_query_service(
        session: AsyncSession = Depends(get_db)
) -> UserQueryService:
    return UserQueryServiceImpl(session)


def get_find_user_by_id_use_case(
        service: UserQueryService = Depends(get_user_query_service)
) -> FindByIdUserUseCase:
    return FindByIdUserUseCaseImpl(service)


def get_tweet_me_use_case(
        service: UserQueryService = Depends(get_user_query_service)
) -> UserGetMeUseCase:
    return UserGetMeUseCaseImpl(service)


def get_delete_following_use_case(
        user_unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work),
) -> DeleteFollowingUseCase:
    return DeleteFollowingUseCaseImpl(user_unit_of_work)


def get_create_following_use_case(
        user_unit_of_work: UserUnitOfWork = Depends(get_user_unit_of_work)
) -> CreateFollowerUseCase:
    return CreateFollowerUseCaseImpl(user_unit_of_work)
