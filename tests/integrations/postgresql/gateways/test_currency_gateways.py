import pytest

from cryptocurrency_parser.src.application.common.transaction_manager import TransactionManager
from cryptocurrency_parser.src.application.currency.currency_gateway import CurrencyReader, CurrencyRemover, CurrencyWriter
# from cryptocurrency_parser.src.infrastructure.database.currency.currency_gateways import 


@pytest.fixture
def user_reader_gateway() -> CurrencyReader:
    ...