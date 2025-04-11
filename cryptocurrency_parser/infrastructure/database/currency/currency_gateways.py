from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from application.currency.currency_gateway import (
    CurrencyAdder,
    CurrencyReader,
    CurrencyRemover,
)
from domain.models.currency.currency import Currency
from domain.models.currency.currency_id import CurrencyId
from infrastructure.persistence.models.currency import (
    CurrencyModel,
    currencies_table,
)


class SQLAlchemyCurrencyReader(CurrencyReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_currency_by_id(
        self,
        currency_id: CurrencyId,
    ) -> Currency | None:
        return await self._session.get(Currency, currency_id)

    async def get_currency_by_ticker(
        self,
        currency_ticker: str,
    ) -> Currency | None:
        query = select(Currency).where(
            currencies_table.c.ticker == currency_ticker,
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()


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

    async def remove_currency_by_id(self, currency_id: CurrencyId) -> None:
        query = delete(CurrencyModel).where(CurrencyModel.id == currency_id)
        await self._session.execute(query)

    async def remove_currency_by_ticker(self, currency_ticker: str) -> None:
        query = delete(CurrencyModel).where(
            CurrencyModel.ticker == currency_ticker,
        )
        await self._session.execute(query)
