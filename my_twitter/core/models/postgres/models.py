from sqlalchemy import Integer
from sqlalchemy.ext.declarative import as_declarative, declarative_base
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


# @as_declarative()
# class Base:
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)


class Base(DeclarativeBase):
    pass
