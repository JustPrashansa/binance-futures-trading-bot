# Binance Futures Trading Bot

## Overview

A Python CLI application that places Market and Limit orders on Binance Futures Demo/Testnet.

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- Input validation
- Logging
- Error handling
- Modular architecture

## Project Structure

trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
│
├── logs/
├── cli.py
├── .env
├── requirements.txt
└── README.md

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Example Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Assumptions

- Binance Futures Demo/Testnet account is configured.
- API credentials have Futures permissions enabled.