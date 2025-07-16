from typing import List, TYPE_CHECKING

from sqlalchemy import String, Table, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.postgres.models import Base
from features.user.domain.entities.user_entity import UserEntity
from features.user.domain.entities.user_query_model import UserReadModel, FollowingReadModel, FollowerReadModel, \
    UserScheme

if TYPE_CHECKING:
    from features.like.data.models.like import Like
    from features.tweet.data.models.tweet import Tweet

follows = Table(
    "follows",
    Base.metadata,
    Column("follower_id", ForeignKey("user.id"), primary_key=True),
    Column("following_id", ForeignKey("user.id"), primary_key=True),
)


class User(Base):
    """
    Модель пользователя для Twitter-клона.
    Содержит связи с твитами, лайками, подписчиками и подписками.
    """
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nickname: Mapped[str] = mapped_column(String(30), unique=True)
    api_key: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)

    likes: Mapped[List['Like']] = relationship(
        "Like",
        back_populates="user",
        cascade="save-update, merge, delete, delete-orphan",
    )

    tweets: Mapped[List['Tweet']] = relationship(
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
            api_key=self.api_key,
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

