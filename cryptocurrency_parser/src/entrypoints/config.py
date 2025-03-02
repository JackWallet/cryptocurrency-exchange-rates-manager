import os

from dataclasses import dataclass


class EnvironmentVariableInaccessible(ValueError):
    name: str

    @property
    def message(self) -> str:
        return f"Env variable with key {self.name} is inaccessible"


@dataclass
class CoinmarketcapConfig:
    api_link: str
    api_key: str


@dataclass
class DatabaseConfig:
    host: str
    port: str
    user: str
    password: str
    db_name: str

    @property
    def connection_url_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


def get_str_env(key: str) -> str:
    val = os.getenv(key)

    if not val:
        raise EnvironmentVariableInaccessible(key)
    return val


def get_coinmarketcap_config() -> CoinmarketcapConfig:
    api_link = get_str_env("COINMARKETCAP_HOST")
    api_key = get_str_env("COINMARKETCAP_API_KEY")

    return CoinmarketcapConfig(api_link=api_link, api_key=api_key)


def get_postgres_config() -> DatabaseConfig:
    host = get_str_env("POSTGRES_HOST")
    port = get_str_env("POSTGRES_PORT")
    user = get_str_env("POSTGRES_USER")
    password = get_str_env("POSTGRES_PASSWORD")
    db_name = get_str_env("POSTGRES_DB_NAME")

    return DatabaseConfig(
        host=host, port=port, user=user, password=password, db_name=db_name
    )
