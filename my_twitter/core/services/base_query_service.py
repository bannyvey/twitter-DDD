from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')


class BaseQueryService(ABC, Generic[T]):
    @abstractmethod
    async def findall(self) -> List[T]:
        raise NotImplementedError()
