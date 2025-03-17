from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyAdder,
)
from cryptocurrency_parser.domain.models.currency.currency import Currency


@dataclass(frozen=True)
class NewCurrencyDTO:
    ticker: str
    full_name: str
    max_supply: int | None
    circulating_supply: int


class AddCurrency(Interactor[NewCurrencyDTO, None]):
    def __init__(
        self,
        currency_db_gateway: CurrencyAdder,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_db_gateway = currency_db_gateway
        self._transaction_manager = transaction_manager

    async def __call__(self, data: NewCurrencyDTO) -> None:
        new_currency: Currency = Currency.create(
            ticker=data.ticker,
            full_name=data.full_name,
            max_supply=data.max_supply,
            circulating_supply=data.circulating_supply,
        )

        await self._currency_db_gateway.save_currency(new_currency)
        await self._transaction_manager.commit()
