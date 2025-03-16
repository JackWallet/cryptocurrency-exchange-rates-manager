from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyAdder,
    CurrencyReader,
)
from cryptocurrency_parser.domain.models.currency.currency import Currency
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId
from cryptocurrency_parser.infrastructure.persistence.models.currency import (
    CurrencyModel,
)


class SQLAlchemyCurrencyReader(CurrencyReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_currency(self, currency_id: CurrencyId) -> Currency | None:
        # TODO fix return
        query = select(Currency).where(CurrencyModel.id == currency_id)
        result = await self._session.execute(query)
        currency = result.scalar_one_or_none()
        return currency if currency else None


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
