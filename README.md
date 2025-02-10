# cryptocurrency-parser

# TODO 
- [ ] REST API for the wallet
  - [ ] Price History of the coin in USD
- [ ] systemd-timers service to put the results to db
- [ ] Dockerise with PosrgreSQL
- [ ] Redis 

# ENV Variables you want to use:
- COINMARKETCAP_HOST
  - "https://pro-api.coinmarketcap.com" for the real coinmarketcap API 
  - "https://sandbox-api.coinmarketcap.com" for the sandbox(test) coinmarketcap API
  
- COINMARKETCAP_API_KEY
  - "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c" for accessing the test api

- POSTGRES_HOST
- POSTGRES_PORT
- POSTGRES_USER
- POSTGRES_PASSWORD