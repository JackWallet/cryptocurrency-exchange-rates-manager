from dataclasses import dataclass

from application.common.interactor import Interactor
from application.common.transaction_manager import (
    TransactionManager,
)
from application.currency.currency_gateway import (
    CurrencyRemover,
)
from domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class RemoveCurrencyByIdDTO:
    currency_id: CurrencyId


class RemoveCurrencyById(Interactor[RemoveCurrencyByIdDTO, None]):
    def __init__(
        self,
        currency_remover: CurrencyRemover,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_remover = currency_remover
        self._transaction_manager = transaction_manager

    async def __call__(self, data: RemoveCurrencyByIdDTO) -> None:
        await self._currency_remover.remove_currency_by_id(
            currency_id=data.currency_id,
        )
        await self._transaction_manager.commit()
