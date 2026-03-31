from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db import Base
from sqlalchemy import JSON, DateTime, func
from sqlalchemy import Integer
from sqlalchemy import Text
from datetime import datetime

class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    section: Mapped[str] = mapped_column(String(200), nullable=False)
    data: Mapped[str] = mapped_column(Text, nullable=False)  # ← Храним JSON как строку
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=func.now(), 
        nullable=False
    )