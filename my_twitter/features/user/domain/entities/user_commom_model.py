from typing import List

from pydantic import BaseModel, Field, ConfigDict


class FollowersScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    id: int
    nickname: str = Field(alias="name")


class FollowingScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    id: int
    nickname: str = Field(alias="name")


class UserScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    id: int
    nickname: str = Field(alias="name")
    followers: List[FollowersScheme]
    following: List[FollowingScheme]


class ResponseUserScheme(BaseModel):
    result = True
    user = UserScheme
