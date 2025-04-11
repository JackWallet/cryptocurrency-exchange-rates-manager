from sqlalchemy import Column, DateTime, Integer, String, Table, func

from domain.models.currency.currency import Currency
from infrastructure.persistence.models.base import mapper_registry

currencies_table = Table(
    "currencies",
    mapper_registry.metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
    ),
    Column(
        "ticker",
        String(4),
    ),
    Column(
        "full_name",
        String(20),
        unique=True,
    ),
    Column(
        "max_supply",
        Integer,
        nullable=True,
    ),
    Column("circulating_supply", Integer),
    Column(
        "last_updated",
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    ),
)

mapper_registry.map_imperatively(Currency, currencies_table)
