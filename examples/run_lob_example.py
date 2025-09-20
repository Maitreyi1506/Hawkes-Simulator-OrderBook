from lob_simulator import OrderBook
import random

if __name__ == "__main__":
    lob = OrderBook()
    # add some random orders
    for _ in range(10):
        side = random.choice(["buy", "sell"])
        price = random.randint(95, 105)
        size = random.randint(1, 5)
        lob.add_limit_order(side, price, size)

    print("Best bid/ask:", lob.best_bid_ask())
    trades = lob.match()
    print("Trades executed:", trades)
