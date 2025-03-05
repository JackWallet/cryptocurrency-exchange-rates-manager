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
        query = select(Currency).where(CurrencyModel.id == currency_id)
        result = await self._session.execute(query)
        currency = result.scalar_one_or_none()
        return currency if currency else None
