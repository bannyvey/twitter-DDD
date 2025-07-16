from core.unit_of_work.unit_of_work import AbstractUnitOfWork
from features.like.domain.repositories.like_repository import LikeRepository


class LikeUnitOfWork(AbstractUnitOfWork[LikeRepository]):
    pass
