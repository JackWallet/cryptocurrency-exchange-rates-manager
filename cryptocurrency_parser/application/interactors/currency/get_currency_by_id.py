from dataclasses import dataclass

from application.common.interactor import Interactor
from application.currency.currency_gateway import (
    CurrencyReader,
)
from application.currency.exceptions import CurrencyNotFoundByIdError
from domain.models.currency.currency import Currency
from domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class GetCurrencyByIdDTO:
    currency_id: CurrencyId


@dataclass(frozen=True)
class GetCurrencyByIdResultDTO:
    currency: Currency


class GetCurrencyById(
    Interactor[GetCurrencyByIdDTO, GetCurrencyByIdResultDTO],
):
    def __init__(
        self,
        currency_reader: CurrencyReader,
    ) -> None:
        self._currency_reader = currency_reader

    async def __call__(
        self,
        data: GetCurrencyByIdDTO,
    ) -> GetCurrencyByIdResultDTO:
        currency = await self._currency_reader.get_currency_by_id(
            currency_id=data.currency_id,
        )
        if currency is None:
            raise CurrencyNotFoundByIdError(identifier=str(data.currency_id))
        return GetCurrencyByIdResultDTO(currency=currency)
