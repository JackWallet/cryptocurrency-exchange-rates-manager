class EntityNotFoundError(Exception):
    """Raised when an entity cannot be found by its identifier."""

    def __init__(self, entity_type: str, entity_id: int):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.message = f"{entity_type} with ID {entity_id} not found"
        super().__init__(self.message)
