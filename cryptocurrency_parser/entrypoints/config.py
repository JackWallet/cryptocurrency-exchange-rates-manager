import os
from dataclasses import dataclass

from entrypoints.exceptions import ConfigError

POSTGRES_HOST_ENV: str = "POSTGRES_HOST"
POSTGRES_PORT_ENV: str = "POSTGRES_PORT"
POSTGRES_USER_ENV: str = "POSTGRES_USER"
POSTGRES_PASSWORD_ENV: str = "POSTGRES_PASSWORD"  # noqa: S105 (Not a password but an env alias)
POSTGRES_DB_NAME_ENV: str = "POSTGRES_DB_NAME"


def get_str_from_env(key: str) -> str:
    if value := os.getenv(key):
        return value
    raise ConfigError(variable_name=key)


@dataclass(frozen=True)
class PostgresConfig:
    host: str
    port: str
    user: str
    password: str
    db: str

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"

    @staticmethod
    def from_env() -> "PostgresConfig":
        env_variables: dict[str, str] = {
            "host": get_str_from_env(POSTGRES_HOST_ENV),
            "port": get_str_from_env(POSTGRES_PORT_ENV),
            "user": get_str_from_env(POSTGRES_USER_ENV),
            "password": get_str_from_env(POSTGRES_PASSWORD_ENV),
            "db": get_str_from_env(POSTGRES_DB_NAME_ENV),
        }

        return PostgresConfig(**env_variables)


@dataclass(frozen=True)
class Config:
    postgres_config: PostgresConfig


def load_config() -> Config:
    return Config(postgres_config=PostgresConfig.from_env())
