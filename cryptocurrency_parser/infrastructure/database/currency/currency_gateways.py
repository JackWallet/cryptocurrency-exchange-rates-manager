from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cryptocurrency_parser.application.currency.currency_gateway import (
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
        query = select(CurrencyModel).where(CurrencyModel.id == currency_id)
        result = await self._session.execute(query)
        currency = result.scalar_one_or_none()
        return Currency(
            id=CurrencyId(currency.id),
            ticker=currency.ticker,
            full_name=currency.full_name,
            max_supply=currency.max_supply,
            circulating_supply=currency.circulating_supply,
            last_updated=currency.last_updated
        ) if currency else None