class EntityNotFoundError(ValueError):
    def __init__(self, entity_name: str, entity_id: str) -> None:
        self._entity_name = entity_name
        self._entity_id = entity_id

    def __str__(self) -> str:
        return (
            f"The {self._entity_name} with id {self._entity_id} wasn't found"
        )


class PriceHistoryRecordNotFoundError(EntityNotFoundError):
    def __init__(self, entity_name: str, entity_id: str) -> None:
        super().__init__(entity_name, entity_id)

    def __str__(self) -> str:
        return super().__str__()


class CurrencyNotFoundError(EntityNotFoundError):
    def __init__(self, entity_name: str, entity_id: str) -> None:
        super().__init__(entity_name, entity_id)

    def __str__(self) -> str:
        return super().__str__()
