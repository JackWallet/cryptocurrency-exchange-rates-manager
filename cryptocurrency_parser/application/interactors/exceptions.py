class EntityNotFoundError(ValueError):
    def __init__(self, entity_id: str) -> None:
        self._entity_id = entity_id


class PriceHistoryRecordNotFoundError(EntityNotFoundError):
    def __init__(self, entity_id: str) -> None:
        super().__init__(entity_id)

    def __str__(self) -> str:
        return (
            f"The price history record with id {self._entity_id} wasn't found"
        )


class CurrencyNotFoundError(EntityNotFoundError):
    def __init__(self, entity_id: str) -> None:
        super().__init__(entity_id)

    def __str__(self) -> str:
        return f"Currency with id {self._entity_id} wasn't found"
