from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base


class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(4))
    full_name: Mapped[str] = mapped_column(String(20), unique=True)
    max_supply: Mapped[Optional[int]]
    circulating_supply: Mapped[int]
    last_updated: Mapped[Optional[datetime]]