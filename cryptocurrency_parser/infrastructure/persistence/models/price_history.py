from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from cryptocurrency_parser.infrastructure.persistence.models.base import Base


class PriceHistoryModel(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    currency_id: Mapped[int] = mapped_column(
        ForeignKey("currencies.id"), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(nullable=False)
    market_cap: Mapped[Decimal] = mapped_column(
        Numeric(precision=24, scale=16), nullable=False
    )
    market_cap_dominance: Mapped[float] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(
        Numeric(precision=24, scale=24), nullable=False
    )
    volume_24h: Mapped[Decimal] = mapped_column(
        Numeric(precision=24, scale=16), nullable=False
    )
    max_supply: Mapped[int | None]
    circulating_supply: Mapped[int]
    percent_change_1h: Mapped[float] = mapped_column(nullable=False)
    percent_change_24h: Mapped[float] = mapped_column(nullable=False)
    percent_change_30d: Mapped[float] = mapped_column(nullable=False)
    percent_change_60d: Mapped[float] = mapped_column(nullable=False)
    percent_change_7d: Mapped[float] = mapped_column(nullable=False)
    percent_change_90d: Mapped[float] = mapped_column(nullable=False)
