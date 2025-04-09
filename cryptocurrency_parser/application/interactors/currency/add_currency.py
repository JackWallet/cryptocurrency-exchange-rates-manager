from dataclasses import dataclass

from application.common.interactor import Interactor
from application.common.transaction_manager import (
    TransactionManager,
)
from application.currency.currency_gateway import (
    CurrencyAdder,
    CurrencyReader,
)
from application.currency.exceptions import (
    CurrencyTickerAlreadyInDatabaseError,
)
from domain.models.currency.currency import Currency


@dataclass(frozen=True)
class AddCurrencyDTO:
    ticker: str
    full_name: str
    max_supply: int | None
    circulating_supply: int


class AddCurrency(Interactor[AddCurrencyDTO, None]):
    def __init__(
        self,
        currency_reader: CurrencyReader,
        currency_adder: CurrencyAdder,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_adder = currency_adder
        self._transaction_manager = transaction_manager
        self._currency_reader = currency_reader

    async def __call__(self, data: AddCurrencyDTO) -> None:
        if (
            await self._currency_reader.get_currency_by_ticker(
                currency_ticker=data.ticker,
            )
            is not None
        ):
            raise CurrencyTickerAlreadyInDatabaseError(ticker=data.ticker)

        new_currency: Currency = Currency.create(
            ticker=data.ticker,
            full_name=data.full_name,
            max_supply=data.max_supply,
            circulating_supply=data.circulating_supply,
        )

        await self._currency_adder.save_currency(new_currency)
        await self._transaction_manager.commit()
