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
    PriceHistoryModel,
)


class SQLAlchemyPriceHistoryReader(PriceHistoryReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_domain(
        self,
        price_history_model: PriceHistoryModel,
    ) -> PriceHistory:
        return PriceHistory(
            id=PriceHistoryId(price_history_model.id),
            currency_id=CurrencyId(price_history_model.currency_id),
            updated_at=price_history_model.updated_at,
            market_cap=price_history_model.market_cap,
            market_cap_dominance=price_history_model.market_cap_dominance,
            price=price_history_model.price,
            volume_24h=price_history_model.volume_24h,
            circulating_supply=price_history_model.circulating_supply,
            percent_change_1h=price_history_model.percent_change_1h,
            percent_change_24h=price_history_model.percent_change_24h,
            percent_change_7d=price_history_model.percent_change_7d,
            percent_change_30d=price_history_model.percent_change_30d,
            percent_change_60d=price_history_model.percent_change_60d,
            percent_change_90d=price_history_model.percent_change_90d,
        )

    async def get_price_history_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> PriceHistory | None:
        query = select(PriceHistoryModel).where(
            PriceHistoryModel.id == price_history_id,
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return (
            self._to_domain(price_history_model=price_history)
            if price_history
            else None
        )

    async def get_price_history_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> list[PriceHistory] | None:
        query = select(PriceHistoryModel).where(
            PriceHistoryModel.currency_id == currency_id,
        ).limit(10)
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return (
            [self._to_domain(record) for record in list(price_history)]
            if price_history
            else None
        )

    async def get_price_history_by_currency_ids(
        self,
        currency_ids: list[CurrencyId],
    ) -> list[PriceHistory] | None:
        query = select(PriceHistoryModel).where(
            and_(PriceHistoryModel.currency_id.in_(currency_ids)),
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalars()
        return (
            [self._to_domain(record) for record in list(price_history)]
            if price_history
            else None
        )

    async def get_highest_recorded_price_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> PriceHistory | None:
        query = (
            select(PriceHistoryModel)
            .where(PriceHistoryModel.currency_id == currency_id)
            .order_by(PriceHistoryModel.price.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return (
            self._to_domain(price_history_model=price_history)
            if price_history
            else None
        )

    async def get_last_record_by_currency_id(
        self,
        currency_id: CurrencyId,
    ) -> PriceHistory | None:
        query = (
            select(PriceHistoryModel)
            .where(PriceHistoryModel.currency_id == currency_id)
            .order_by(PriceHistoryModel.updated_at.desc())
            .limit(1)
        )
        query_result = await self._session.execute(query)
        price_history = query_result.scalar_one_or_none()
        return (
            self._to_domain(price_history_model=price_history)
            if price_history
            else None
        )


class SQLAlchemyPriceHistoryAdder(PriceHistoryAdder):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_model(
        self,
        price_history: PriceHistory,
    ) -> PriceHistoryModel:
        return PriceHistoryModel(
            id=price_history.id,
            currency_id=CurrencyId(price_history.currency_id),
            updated_at=price_history.updated_at,
            market_cap=price_history.market_cap,
            market_cap_dominance=price_history.market_cap_dominance,
            price=price_history.price,
            volume_24h=price_history.volume_24h,
            circulating_supply=price_history.circulating_supply,
            percent_change_1h=price_history.percent_change_1h,
            percent_change_24h=price_history.percent_change_24h,
            percent_change_7d=price_history.percent_change_7d,
            percent_change_30d=price_history.percent_change_30d,
            percent_change_60d=price_history.percent_change_60d,
            percent_change_90d=price_history.percent_change_90d,
        )

    async def add_price_history_record(
        self,
        price_history: PriceHistory,
    ) -> None:
        price_history_model: PriceHistoryModel = self._to_model(
            price_history=price_history,
        )
        self._session.add(price_history_model)


class SQLAlchemyPriceHistoryRemover(PriceHistoryRemover):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def remove_price_history_record_by_id(
        self,
        price_history_id: PriceHistoryId,
    ) -> None:
        query = delete(PriceHistoryModel).where(
            PriceHistoryModel.id == price_history_id,
        )
        await self._session.execute(query)
