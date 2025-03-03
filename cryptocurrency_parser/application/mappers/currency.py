from infrastructure.persistence.models.currency import CurrencyModel


class CurrencyMapper:
    @staticmethod
    def orm_to_domain(orm_model: CurrencyModel) -> None:
        ...