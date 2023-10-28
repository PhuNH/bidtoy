from typing import Optional

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Impression(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    profile: Mapped[str] = mapped_column(String, index=True)
    bid: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_won: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
