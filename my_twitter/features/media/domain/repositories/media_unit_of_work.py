from my_twitter.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from my_twitter.features.media.domain.repositories.media_repository import MediaRepository


class MediaUnitOfWork(AbstractUnitOfWork[MediaRepository]):
    pass
