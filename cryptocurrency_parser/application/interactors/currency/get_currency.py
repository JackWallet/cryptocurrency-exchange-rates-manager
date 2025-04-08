from dataclasses import dataclass

from application.common.interactor import Interactor
from application.common.transaction_manager import (
    TransactionManager,
)
from application.currency.currency_gateway import (
    CurrencyReader,
)
from application.interactors.exceptions import (
    CurrencyNotFoundError,
)
from domain.models.currency.currency import Currency
from domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class GetCurrencyDTO:
    currency_id: CurrencyId


@dataclass(frozen=True)
class GetCurrencyResultDTO:
    currency: Currency


class GetCurrency(Interactor[GetCurrencyDTO, GetCurrencyResultDTO]):
    def __init__(
        self,
        currency_reader: CurrencyReader,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_reader = currency_reader
        self._transaction_manager = transaction_manager

    async def __call__(self, data: GetCurrencyDTO) -> GetCurrencyResultDTO:
        currency = await self._currency_reader.get_currency_by_id(
            currency_id=data.currency_id,
        )
        if currency is None:
            raise CurrencyNotFoundError(entity_id=str(data.currency_id))
        return GetCurrencyResultDTO(currency=currency)
