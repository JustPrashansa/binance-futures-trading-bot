import argparse
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logger
logger = setup_logger()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    args = parser.parse_args()
    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        client = BinanceFuturesClient().client
        manager = OrderManager(client)
        print("\nORDER REQUEST")
        print("--------------------")
        print("Symbol:", args.symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", args.quantity)
        if order_type == "MARKET":
            response = manager.market_order(
                args.symbol,
                side,
                args.quantity
            )
        else:
            if not args.price:
                raise ValueError(
                    "Price required for LIMIT order"
                )
            response = manager.limit_order(
                args.symbol,
                side,
                args.quantity,
                args.price
            )
        print("\nSUCCESS")
        print("--------------------")
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])
        print("Order Type:", response["type"])
        print("Side:", response["side"])
        if "price" in response:
            print("Price:", response["price"])
    except Exception as e:
        logger.error(str(e))
        print("\nFAILED")
        print(str(e))
if __name__ == "__main__":
    main()