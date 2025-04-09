from dataclasses import dataclass

from application.common.interactor import Interactor
from application.common.transaction_manager import (
    TransactionManager,
)
from application.currency.currency_gateway import (
    CurrencyReader,
    CurrencyRemover,
)
from application.currency.exceptions import CurrencyNotFoundByIdError
from domain.models.currency.currency_id import CurrencyId


@dataclass(frozen=True)
class RemoveCurrencyByIdDTO:
    currency_id: CurrencyId


class RemoveCurrencyById(Interactor[RemoveCurrencyByIdDTO, None]):
    def __init__(
        self,
        currency_remover: CurrencyRemover,
        currency_reader: CurrencyReader,
        transaction_manager: TransactionManager,
    ) -> None:
        self._currency_remover = currency_remover
        self._transaction_manager = transaction_manager
        self._currency_reader = currency_reader

    async def __call__(self, data: RemoveCurrencyByIdDTO) -> None:
        if (
            await self._currency_reader.get_currency_by_id(
                currency_id=data.currency_id,
            )
            is None
        ):
            raise CurrencyNotFoundByIdError(identifier=data.currency_id)

        await self._currency_remover.remove_currency_by_id(
            currency_id=data.currency_id,
        )
        await self._transaction_manager.commit()
