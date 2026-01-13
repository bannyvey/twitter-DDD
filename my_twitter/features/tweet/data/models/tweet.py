from datetime import datetime
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_twitter.core.models.postgres.models import Base
from my_twitter.features.tweet.domain.entities.tweet_entity import TweetEntity
from my_twitter.features.tweet.domain.entities.tweet_query_model import AuthorReadModel, MediaReadModel, LikeReadModel, \
    TweetReadModel

if TYPE_CHECKING:
    from my_twitter.features.like import Like
    from my_twitter.features.media import Media
    from my_twitter.features.user import User


class Tweet(Base):
    __tablename__ = 'table_tweet'
    message: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    author: Mapped["User"] = relationship("User", back_populates="tweets")

    likes: Mapped[List["Like"]] = relationship(
        'Like',
        back_populates="tweet",
        cascade="save-update, merge, delete, delete-orphan",
    )

    medias: Mapped[List["Media"]] = relationship(
        "Media",
        back_populates="tweet",
        cascade="save-update, merge, delete, delete-orphan",
    )

    def to_entity(self) -> TweetEntity:
        return TweetEntity(
            id_=self.id,
            message=self.message,
            created_at=self.created_at,
            user_id=self.user_id
        )

    async def to_read_model(self):
        author_model = AuthorReadModel(
            id=self.author.id,
            name=self.author.nickname
        )
        media_models = [MediaReadModel(path=media.path) for media in self.medias]
        like_models = [
            LikeReadModel(
                user_id=like.user_id,
                name=like.user.nickname if like.user else "Unknown"
            )
            for like in self.likes
        ]
        return TweetReadModel(
            id=self.id,
            content=self.message,
            attachments=media_models,
            author=author_model,
            likes=like_models
        )

    @staticmethod
    async def from_entity(tweet: TweetEntity) -> 'Tweet':
        return Tweet(
            id=tweet.id_,
            message=tweet.message,
            created_at=tweet.created_at,
            user_id=tweet.user_id
        )
