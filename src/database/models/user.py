from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import BaseModel

if TYPE_CHECKING:
    from src.database.models.notes import Note


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    role_level: Mapped[int] = mapped_column(default=0, server_default="0")
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(), server_default=func.now()
    )

    notes: Mapped[list["Note"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, tg_chat_id={self.tg_chat_id}, role={self.role_level})>"
