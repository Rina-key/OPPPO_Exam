from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db import Base
from sqlalchemy import JSON, DateTime, func
from sqlalchemy import Integer
from sqlalchemy import Text
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(90), nullable=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    group: Mapped[str] = mapped_column(String(50), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    birth: Mapped[str] = mapped_column(String(20), nullable=True)
    education: Mapped[str] = mapped_column(String(100), nullable=True)
    vk: Mapped[str] = mapped_column(String(100), nullable=True)
    tg: Mapped[str] = mapped_column(String(100), nullable=True)


# class Submission(Base):
#     __tablename__ = "submissions"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     section: Mapped[str] = mapped_column(String(200), nullable=False)
#     data: Mapped[str] = mapped_column(Text, nullable=False)  # ← Храним JSON как строку
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime, 
#         server_default=func.now(), 
#         nullable=False
#     )