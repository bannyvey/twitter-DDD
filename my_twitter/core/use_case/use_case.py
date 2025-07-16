from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')
R = TypeVar('R')


class BaseUseCase(ABC, Generic[T, R]):
    @abstractmethod
    async def __call__(self, args: T | None = None) -> R | None:
        raise NotImplementedError
