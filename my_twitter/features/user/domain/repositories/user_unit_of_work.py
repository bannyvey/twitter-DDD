from my_twitter.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from my_twitter.features.user.domain.repositories.user_repository import UserRepository


class UserUnitOfWork(AbstractUnitOfWork[UserRepository]):
    pass
