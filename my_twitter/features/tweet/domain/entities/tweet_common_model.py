from typing import List
from pydantic import BaseModel, ConfigDict, Field, computed_field


class AuthorSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class LikeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    name: str


class MediaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    path: str


class TweetSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    medias: List[MediaSchema] = Field(alias='attachments')
    author: AuthorSchema
    likes: List[LikeSchema]

    @computed_field
    @property
    def attachments(self) -> List[str]:
        return [media.path for media in self.medias]


class AllTweetsResponseScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    result: bool = True
    tweets: List[TweetSchema]
