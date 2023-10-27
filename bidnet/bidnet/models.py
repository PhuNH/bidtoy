from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Impression(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    profile: Mapped[str] = mapped_column(String(20), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, index=True, default=datetime.utcnow)
    bidder_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey('bidder.id'), nullable=True)

    def __repr__(self):
        bidder_part = 'no one' if not self.bidder_id else f'bidder {self.bidder_id}'
        return f'Impression with profile {self.profile} created at {self.created_at} belonging to {bidder_part}'


class Bidder(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    addr: Mapped[str] = mapped_column(String, index=True, unique=True)
