from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    url: str

    @classmethod
    def default_asyncpg(
        cls, db_name: str, username: str, password: str, host: str, port: str
    ) -> "DatabaseConfig":
        return cls(
            url=f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{db_name}"
        )
