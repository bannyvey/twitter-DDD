from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class AbstractUnitOfWork(ABC, Generic[T]):
    repository: T

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError
