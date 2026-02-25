import argparse
from client import get_binance_client
from orders import place_futures_order
from logging_config import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    
    parser.add_argument('--symbol', type=str, required=True, help='Target symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--qty', type=float, required=True, help='Quantity to trade')
    parser.add_argument('--price', type=float, help='Price (Required for LIMIT orders)')

    args = parser.parse_args()

    client = get_binance_client()

    if args.type.upper() == 'LIMIT' and args.price is None:
        logger.error("Error: LIMIT ORDER -- entering price is mandatory.")
        return

    response = place_futures_order(
        client, 
        args.symbol, 
        args.side, 
        args.type, 
        args.qty, 
        args.price
    )

    if response:
        print("\n--- ORDER SUMMARY ---")
        print(f"Status: SUCCESS")
        print(f"OrderID: {response.get('orderId')}")
        print(f"Symbol: {response.get('symbol')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print("----------------------\n")
    else:
        print("\n--- ORDER FAILED ---")

if __name__ == "__main__":
    main()