from dataclasses import dataclass
from pydantic import BaseModel, computed_field, ConfigDict
from typing import List


@dataclass
class AuthorReadModel:
    id: int
    name: str


@dataclass
class LikeReadModel:
    user_id: int
    name: str


@dataclass
class MediaReadModel:
    path: str


@dataclass
class TweetReadModel:
    id: int
    content: str
    attachments: List[MediaReadModel]
    author: AuthorReadModel
    likes: List[LikeReadModel]


# class AuthorSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True, populate_by_name=True)
#     id: int
#     name: str
#
#
# class LikeSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#     id: int
#     name: AuthorSchema
#
#
# class MediaSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#     path: str
#
#
# class TweetSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True, populate_by_name=True)
#     id: int
#     content: str
#     attachments: List[MediaSchema]
#     author: AuthorSchema
#     likes: List[LikeSchema]
#
#     @computed_field
#     @property
#     def attachments(self) -> List[str]:
#         return [media.path for media in self._attachments]
#
#
# class TweetReadModel(TweetSchema):
#     pass
