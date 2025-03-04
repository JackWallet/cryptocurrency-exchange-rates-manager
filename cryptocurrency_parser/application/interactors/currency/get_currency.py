from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyReader,
)
from cryptocurrency_parser.domain.models.currency.currency import Currency
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class GetCurrencyDTO:
    currency_id: CurrencyId


class RemoveCurrency(Interactor[GetCurrencyDTO, Currency]):
    def __init__(
        self,
        currency_db_gateway: CurrencyReader,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_db_gateway = currency_db_gateway
        self._transaction_manager = transaction_manager

    async def __call__(self, data: GetCurrencyDTO) -> Currency:
        return await self._currency_db_gateway.get_currency(
            currency_id=data.currency_id
        )
