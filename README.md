# Cryptocurrency Exchange Rates Manager

![Checks Status](https://github.com/JackWallet/cryptocurrency-exchange-rates-manager/actions/workflows/poetry.yml/badge.svg)
![Checks Status](https://github.com/JackWallet/cryptocurrency-exchange-rates-manager/actions/workflows/codeql.yml/badge.svg)

# TODO 
- [x] REST API for the wallet
  - [x] Price History of the coin in USD
  - [x] Alembic migrations
  - [x] Repository with crud methods for the DB
- [ ] Docker
- [ ] Redis
- [ ] Id Provider support for the authentification
- [ ] Tests
  - [x] Unit
  - [ ] E2E
- [ ] Set up GitHub Actions support
- [x] Rewrite ORM declarative mapping to imperative one
# ENV Variables you want to use:
- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB_NAME
