from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.models.base import Base


class TradingPair(Base):
    __tablename__ = "trading_pairs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    base_currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    quote_currency_id: Mapped[int] = mapped_column(ForeignKey("currency.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
