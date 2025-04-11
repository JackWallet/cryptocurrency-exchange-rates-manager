from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    Table,
    func,
)

from domain.models.price_history.price_history import PriceHistory
from infrastructure.persistence.models.base import mapper_registry

price_history_table = Table(
    "price_history",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column(
        "currency_id",
        ForeignKey("currencies.id"),
        nullable=False,
    ),
    Column("updated_at", DateTime, onupdate=func.now(), nullable=False),
    Column("market_cap", Numeric(precision=24, scale=16), nullable=False),
    Column("market_cap_dominance", Float, nullable=False),
    Column("price", Numeric(precision=24, scale=24), nullable=False),
    Column("volume_24h", Numeric(precision=24, scale=16), nullable=False),
    Column("circulating_supply", Integer),
    Column("percent_change_1h", Float, nullable=False),
    Column("percent_change_24h", Float, nullable=False),
    Column("percent_change_30d", Float, nullable=False),
    Column("percent_change_60d", Float, nullable=False),
    Column("percent_change_7d", Float, nullable=False),
    Column("percent_change_90d", Float, nullable=False),
)

mapper_registry.map_imperatively(PriceHistory, price_history_table)
