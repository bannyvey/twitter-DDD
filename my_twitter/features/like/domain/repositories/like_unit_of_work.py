from my_twitter.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from my_twitter.features.like.domain.repositories.like_repository import LikeRepository


class LikeUnitOfWork(AbstractUnitOfWork[LikeRepository]):
    pass
