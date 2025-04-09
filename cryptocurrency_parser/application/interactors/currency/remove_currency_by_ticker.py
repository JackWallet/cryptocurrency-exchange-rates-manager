from dataclasses import dataclass

from application.common.interactor import Interactor
from application.common.transaction_manager import (
    TransactionManager,
)
from application.currency.currency_gateway import (
    CurrencyReader,
    CurrencyRemover,
)
from application.currency.exceptions import CurrencyNotFoundByTickerError


@dataclass(frozen=True)
class RemoveCurrencyByTickerDTO:
    currency_ticker: str


class RemoveCurrencyByTicker(Interactor[RemoveCurrencyByTickerDTO, None]):
    def __init__(
        self,
        currency_reader: CurrencyReader,
        currency_remover: CurrencyRemover,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_reader = currency_reader
        self._currency_remover = currency_remover
        self._transaction_manager = transaction_manager

    async def __call__(self, data: RemoveCurrencyByTickerDTO) -> None:
        if (
            await self._currency_reader.get_currency_by_ticker(
                currency_ticker=data.currency_ticker,
            )
            is None
        ):
            raise CurrencyNotFoundByTickerError(
                identifier=data.currency_ticker,
            )

        await self._currency_remover.remove_currency_by_ticker(
            currency_ticker=data.currency_ticker,
        )
        await self._transaction_manager.commit()
