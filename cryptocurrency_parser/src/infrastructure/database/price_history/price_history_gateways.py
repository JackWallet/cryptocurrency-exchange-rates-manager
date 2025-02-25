from sqlalchemy import and_, select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from application.price_history.price_history_gateway import (
    PriceHistoryReader,
    PriceHistoryAdder,
    PriceHistoryRemover,
)
from domain.models.currency.currency_id import CurrencyId
from domain.models.price_history.price_history import PriceHistory
from domain.models.price_history.price_history_id import PriceHistoryId
from infrastructure.persistence.models.price_history import (
    PriceHistory as PriceHistoryModel,
)


class SQLAlchemyPriceHistoryReader(PriceHistoryReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, price_history_id: PriceHistoryId) -> PriceHistory | None:
        query = select(PriceHistoryModel).where(
            PriceHistoryModel.id == price_history_id
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return PriceHistory(**price_history.__dict__) if price_history else None

    async def get_by_currency_id(
        self, currency_id: CurrencyId
    ) -> list[PriceHistory] | None:
        query = select(PriceHistoryModel).where(
            PriceHistoryModel.currency_id == currency_id
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return (
            [PriceHistory(**ph.__dict__) for ph in price_history]
            if price_history
            else None
        )

    async def get_by_currency_ids(
        self, currency_ids: list[CurrencyId]
    ) -> list[PriceHistory] | None:
        query = select(PriceHistoryModel).where(
            and_(PriceHistoryModel.currency_id.in_(currency_ids))
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return (
            [PriceHistory(**ph.__dict__) for ph in price_history]
            if price_history
            else None
        )

    async def get_highest_recorded_price_by_currency_id(
        self, currency_id: CurrencyId
    ) -> PriceHistory | None:
        query = (
            select(PriceHistoryModel)
            .where(PriceHistoryModel.currency_id == currency_id)
            .order_by(PriceHistoryModel.price.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return PriceHistory(**price_history.__dict__) if price_history else None
