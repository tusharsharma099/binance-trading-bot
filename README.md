# Binance Futures Trading Bot 

## Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it and install requirements: `pip install -r requirements.txt`.
4. Create a `.env` file with your `BINANCE_API_KEY` and `BINANCE_SECRET_KEY`.

## Usage Examples
- **Market Order:** `python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01`
- **Limit Order:** `python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 50000`

## Implementation Details
- Used `python-binance` library for API interactions.
- Implemented structured logging and error handling.
- Environment: Binance Futures Testnet.