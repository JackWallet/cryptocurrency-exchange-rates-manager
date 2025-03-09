from dataclasses import dataclass

from cryptocurrency_parser.application.common.interactor import Interactor
from cryptocurrency_parser.application.common.transaction_manager import (
    TransactionManager,
)
from cryptocurrency_parser.application.currency.currency_gateway import (
    CurrencyRemover,
)
from cryptocurrency_parser.domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class RemoveCurrencyDTO:
    currency_id: CurrencyId


class RemoveCurrency(Interactor[RemoveCurrencyDTO, None]):
    def __init__(
        self,
        currency_db_gateway: CurrencyRemover,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_db_gateway = currency_db_gateway
        self._transaction_manager = transaction_manager

    async def __call__(self, data: RemoveCurrencyDTO) -> None:
        await self._currency_db_gateway.remove_currency(
            currency_id=data.currency_id,
        )
        await self._transaction_manager.commit()
