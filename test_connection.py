from client import get_binance_client
from logging_config import setup_logging

logger = setup_logging()

def test_conn():
    try:
        client = get_binance_client()
        
        account_info = client.futures_account()
        
        logger.info("Connection Successful! ")
        for asset in account_info['assets']:
            if asset['asset'] == 'USDT':
                logger.info(f"Available Balance: {asset['walletBalance']} USDT")
                
    except Exception as e:
        logger.error(f"Connection Failed: {e}")

if __name__ == "__main__":
    test_conn()