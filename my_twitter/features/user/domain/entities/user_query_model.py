from dataclasses import dataclass
from typing import List


@dataclass
class FollowingReadModel:
    id: int
    name: str


@dataclass
class FollowerReadModel:
    id: int
    name: str


@dataclass
class UserScheme:
    id: int
    name: str
    followers: List[FollowerReadModel]
    following: List[FollowingReadModel]


@dataclass
class UserReadModel:
    result: bool
    user: UserScheme
