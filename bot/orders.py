import logging
logger = logging.getLogger(__name__)
class OrderManager:
    def __init__(self, client):
        self.client = client
    def market_order(self, symbol, side, quantity):
        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market Order: {response}")
        return response
    def limit_order(self, symbol, side, quantity, price):
        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Limit Order: {response}")
        return response