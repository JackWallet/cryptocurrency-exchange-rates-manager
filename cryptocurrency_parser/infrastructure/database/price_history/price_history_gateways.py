from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.price_history.price_history_gateway import (
    PriceHistoryAdder,
    PriceHistoryReader,
    PriceHistoryRemover,
)
from cryptocurrency_parser.domain.exceptions.exceptions import (
    EntityNotFoundError,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.domain.models.price_history.price_history import (
    PriceHistory,
)
from cryptocurrency_parser.domain.models.price_history.price_history_id import (
    PriceHistoryId,
)
from cryptocurrency_parser.infrastructure.persistence.models.price_history import (
    PriceHistoryModel,
)


class SQLAlchemyPriceHistoryReader(PriceHistoryReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> PriceHistory | None:
        query = select(PriceHistory).where(
            PriceHistoryModel.id == price_history_id,
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return price_history if price_history else None

    async def get_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> list[PriceHistory] | None:
        query = select(PriceHistory).where(
            PriceHistoryModel.currency_id == currency_id,
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return list(price_history) if price_history else None

    async def get_by_currency_ids(
        self,
        currency_ids: list[CurrencyId],
    ) -> list[PriceHistory] | None:
        query = select(PriceHistory).where(
            and_(PriceHistoryModel.currency_id.in_(currency_ids)),
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return list(price_history) if price_history else None

    async def get_highest_recorded_price_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> PriceHistory | None:
        query = (
            select(PriceHistory)
            .where(PriceHistoryModel.currency_id == currency_id)
            .order_by(PriceHistoryModel.price.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return price_history if price_history else None

    async def get_last_record(
        self,
        currency_ids: list[CurrencyId],
    ) -> list[PriceHistory]: ...


class SQLAlchemyPriceHistoryAdder(PriceHistoryAdder):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_price_history_record(
        self,
        price_history: PriceHistory,
    ) -> None:
        price_history_model = PriceHistoryModel(
            id=price_history.id,
            currency_id=price_history.currency_id,
            updated_at=price_history.updated_at,
            market_cap=price_history.market_cap,
            market_cap_dominance=price_history.market_cap_dominance,
            price=price_history.price,
            volume_24h=price_history.volume_24h,
        )
        self._session.add(price_history_model)


class SQLAlchemyPriceHistoryRemover(PriceHistoryRemover):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def remove_price_history_record_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> None:
        price_history = await self._session.get(
            PriceHistoryModel,
            price_history_id,
        )
        if price_history:
            await self._session.delete(price_history)
        else:
            raise EntityNotFoundError(
                entity_type="PriceHistory",
                entity_id=price_history_id,
            )
