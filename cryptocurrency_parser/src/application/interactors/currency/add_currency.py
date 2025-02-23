from dataclasses import dataclass
from typing import Optional, Protocol

from application.common.interactor import Interactor
from application.currency.currency_gateway import CurrencyWriter
from cryptocurrency_parser.src.domain.models.currency.currency import Currency
from domain.services.currency.currency import CurrencyService


@dataclass(frozen=True)
class NewCurrencyDTO:
    ticker: str
    full_name: str
    max_supply: Optional[int]
    circulating_supply: int


class AddCurrency(Interactor[NewCurrencyDTO, None]):
    def __init__(
        self, currency_db_gateway: CurrencyWriter, currency_service: CurrencyService
    ) -> None:
        self._currency_db_gateway = currency_db_gateway
        self._currency_service = currency_service

    async def __call__(self, data: NewCurrencyDTO) -> None:
        new_currency: Currency = self._currency_service.create_currency(
            full_name=data.full_name,
            ticker=data.ticker,
        )

        await self._currency_db_gateway.save_currency(new_currency)