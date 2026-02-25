from binance.exceptions import BinanceAPIException
from logging_config import setup_logging

logger = setup_logging()

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Sending Order: {side} {quantity} {symbol} type: {order_type} price: {price}")

        if order_type.upper() == "MARKET":
            # Market Order placement 
            response = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
        elif order_type.upper() == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
        
        logger.info(f"Order Successful! ID: {response.get('orderId')}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        return None
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return None