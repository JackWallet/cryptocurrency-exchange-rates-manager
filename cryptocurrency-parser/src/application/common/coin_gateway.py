from typing import Protocol
from domain.models.coin_id import CoinId
from domain.models.coin import Coin


class CoinReader(Protocol):
    async def get_coin(self, coin_id: CoinId) -> Coin: ...


class CoinSaver(Protocol):
    async def save_coin(self, coin: Coin) -> None: ...


class CoinRemover(Protocol):
    async def remove_coin(self, coin_id: CoinId) -> None: ...
