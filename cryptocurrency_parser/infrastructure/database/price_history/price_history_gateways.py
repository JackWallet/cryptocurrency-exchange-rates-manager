from collections.abc import Sequence

from sqlalchemy import and_, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from application.price_history.price_history_gateway import (
    PriceHistoryAdder,
    PriceHistoryReader,
    PriceHistoryRemover,
)
from domain.models.currency.currency_id import CurrencyId
from domain.models.price_history.price_history import (
    PriceHistory,
)
from domain.models.price_history.price_history_id import (
    PriceHistoryId,
)
from infrastructure.persistence.models.price_history import (
    price_history_table,
)


class SQLAlchemyPriceHistoryReader(PriceHistoryReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_price_history_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> PriceHistory | None:
        return await self._session.get(PriceHistory, price_history_id)

    async def get_price_history_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> list[PriceHistory] | None:
        query = (
            select(PriceHistory)
            .where(
                price_history_table.c.currency_id == currency_id,
            )
            .limit(10)
        )
        query_result = await self._session.execute(query)
        scalars: Sequence[PriceHistory] = query_result.scalars().all()
        if len(scalars) == 0:
            return None

        return list(scalars)

    async def get_price_history_by_currency_ids(
        self,
        currency_ids: list[CurrencyId],
    ) -> list[PriceHistory] | None:
        query = select(PriceHistory).where(
            and_(price_history_table.c.currency_id.in_(currency_ids)),
        )
        query_result = await self._session.execute(query)
        scalars: Sequence[PriceHistory] = query_result.scalars().all()
        if len(scalars) == 0:
            return None

        return list(scalars)

    async def get_highest_recorded_price_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> PriceHistory | None:
        query = (
            select(PriceHistory)
            .where(price_history_table.c.currency_id == currency_id)
            .order_by(price_history_table.c.price.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()

    async def get_last_record_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> PriceHistory | None:
        query = (
            select(PriceHistory)
            .where(price_history_table.c.currency_id == currency_id)
            .order_by(price_history_table.c.updated_at.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()


class SQLAlchemyPriceHistoryAdder(PriceHistoryAdder):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_price_history_record(
        self,
        price_history: PriceHistory,
    ) -> None:
        self._session.add(price_history)


class SQLAlchemyPriceHistoryRemover(PriceHistoryRemover):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def remove_price_history_record_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> None:
        query = delete(PriceHistory).where(
            price_history_table.c.id == price_history_id,
        )
        await self._session.execute(query)
