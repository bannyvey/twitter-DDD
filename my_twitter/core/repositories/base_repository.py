from abc import abstractmethod, ABC
from typing import Generic, TypeVar, Sequence

T = TypeVar('T')
R = TypeVar('R')


class BaseTweetRepository(ABC, Generic[T]):
    @abstractmethod
    async def create(self, entity: T) -> T:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entity: T) -> None:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> Sequence[T]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: T) -> T:
        raise NotImplementedError
