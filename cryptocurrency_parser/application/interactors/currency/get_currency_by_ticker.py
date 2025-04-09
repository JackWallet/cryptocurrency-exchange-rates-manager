from dataclasses import dataclass

from application.common.interactor import Interactor
from application.currency.currency_gateway import (
    CurrencyReader,
)
from application.currency.exceptions import (
    CurrencyNotFoundByTickerError,
)
from domain.models.currency.currency import Currency


@dataclass(frozen=True)
class GetCurrencyByTickerDTO:
    currency_ticker: str


@dataclass(frozen=True)
class GetCurrencyByTickerResultDTO:
    currency: Currency


class GetCurrencyByTicker(
    Interactor[GetCurrencyByTickerDTO, GetCurrencyByTickerResultDTO],
):
    def __init__(
        self,
        currency_reader: CurrencyReader,
    ) -> None:
        self._currency_reader = currency_reader

    async def __call__(
        self,
        data: GetCurrencyByTickerDTO,
    ) -> GetCurrencyByTickerResultDTO:
        currency = await self._currency_reader.get_currency_by_ticker(
            currency_ticker=data.currency_ticker,
        )
        if currency is None:
            raise CurrencyNotFoundByTickerError(
                identifier=str(data.currency_ticker),
            )
        return GetCurrencyByTickerResultDTO(currency=currency)
