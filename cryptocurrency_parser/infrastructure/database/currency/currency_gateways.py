from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyAdder,
    CurrencyReader,
    CurrencyRemover,
)
from cryptocurrency_parser.domain.models.currency.currency import Currency
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.infrastructure.persistence.models.currency import (
    CurrencyModel,
)


class SQLAlchemyCurrencyReader(CurrencyReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_domain(self, currency_model: CurrencyModel) -> Currency:
        return Currency(
            id=CurrencyId(currency_model.id),
            ticker=currency_model.ticker,
            full_name=currency_model.full_name,
            max_supply=currency_model.max_supply,
            circulating_supply=currency_model.circulating_supply,
            last_updated=currency_model.last_updated,
        )

    async def get_currency_by_id(
        self,
        currency_id: CurrencyId,
    ) -> Currency | None:
        query = select(CurrencyModel).where(CurrencyModel.id == currency_id)
        result = await self._session.execute(query)
        currency = result.scalar_one_or_none()

        return (
            self._to_domain(currency)
            if isinstance(currency, CurrencyModel)
            else None
        )

    async def get_currency_by_ticker(
        self,
        currency_ticker: str,
    ) -> Currency | None:
        query = select(CurrencyModel).where(
            CurrencyModel.ticker == currency_ticker,
        )
        result = await self._session.execute(query)
        currency = result.scalar_one_or_none()

        return (
            self._to_domain(currency)
            if isinstance(currency, CurrencyModel)
            else None
        )


class SQLAlchemyCurrencyAdder(CurrencyAdder):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _to_model(self, currency: Currency) -> CurrencyModel:
        return CurrencyModel(
            id=currency.id,
            ticker=currency.ticker,
            full_name=currency.full_name,
            max_supply=currency.max_supply,
            circulating_supply=currency.circulating_supply,
            last_updated=currency.last_updated,
        )

    async def save_currency(self, currency: Currency) -> None:
        currency_model = self._to_model(currency=currency)
        self._session.add(currency_model)


class SQLAlchemyCurrencyRemover(CurrencyRemover):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def remove_currency(self, currency_id: CurrencyId) -> None:
        query = delete(CurrencyModel).where(CurrencyModel.id == currency_id)
        await self._session.execute(query)
