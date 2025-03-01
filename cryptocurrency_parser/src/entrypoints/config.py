import os

from dataclasses import dataclass


@dataclass
class CoinmarketcapConfig:
    api_link: str
    api_key: str

    @staticmethod
    def from_env():
        api_link = os.getenv("COINMARKETCAP_HOST")
        api_key = os.getenv("COINMARKETCAP_API_KEY")

        return CoinmarketcapConfig(api_link=api_link, api_key=api_key)


@dataclass
class PostgresConfig:
    host: str
    port: str
    user: str
    password: str

    @staticmethod
    def from_env():
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")

        return PostgresConfig(host=host, port=port, user=user, password=password)


def get_coinmarketcap_config() -> CoinmarketcapConfig:
    return CoinmarketcapConfig.from_env()


def get_postgres_config() -> PostgresConfig:
    return PostgresConfig.from_env()
