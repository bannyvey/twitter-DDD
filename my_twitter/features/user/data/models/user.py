from typing import List, TYPE_CHECKING

from sqlalchemy import String, Table, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_twitter.core.models.postgres.models import Base
from my_twitter.features.user.data.models.follows import follows
from my_twitter.features.user.domain.entities.user_entity import UserEntity
from my_twitter.features.user.domain.entities.user_query_model import (
    UserReadModel,
    FollowingReadModel,
    FollowerReadModel,
    UserScheme
)

if TYPE_CHECKING:
    from my_twitter.features.like import Like
    from my_twitter.features.tweet import Tweet



class User(Base):
    """
    Модель пользователя для Twitter-клона.
    Содержит связи с твитами, лайками, подписчиками и подписками.
    """
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    nickname: Mapped[str] = mapped_column(String(30), unique=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)

    likes: Mapped[List["Like"]] = relationship(
        "Like",
        back_populates="user",
        cascade="save-update, merge, delete, delete-orphan",
    )

    tweets: Mapped[List["Tweet"]] = relationship(
        "Tweet",
        back_populates="author",
        cascade="save-update, merge, delete, delete-orphan"
    )

    followers: Mapped[List["User"]] = relationship(
        "User",
        secondary=follows,
        primaryjoin="User.id == follows.c.following_id",
        secondaryjoin="User.id == follows.c.follower_id",
        back_populates="following",
    )

    following: Mapped[List["User"]] = relationship(
        "User",
        secondary=follows,
        primaryjoin="User.id == follows.c.follower_id",
        secondaryjoin="User.id == follows.c.following_id",
        back_populates="followers",
    )

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id_=self.id,
            nickname=self.nickname,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    def to_read_model(self) -> UserReadModel:
        following_model = [
            FollowingReadModel(id=user.id, name=user.nickname)
            for user in self.following
        ]
        followers_model = [
            FollowerReadModel(id=user.id, name=user.nickname)
            for user in self.followers
        ]

        user = UserScheme(
            id=self.id,
            name=self.nickname,
            followers=followers_model,
            following=following_model,
        )

        return UserReadModel(
            result=True,
            user=user,
        )

