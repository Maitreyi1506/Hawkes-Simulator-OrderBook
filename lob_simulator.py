import heapq
import random

class OrderBook:
    def __init__(self):
        self.bids = []  # max-heap
        self.asks = []  # min-heap

    def add_limit_order(self, side, price, size):
        if side == "buy":
            heapq.heappush(self.bids, (-price, size))
        else:
            heapq.heappush(self.asks, (price, size))

    def match(self):
        trades = []
        while self.bids and self.asks and -self.bids[0][0] >= self.asks[0][0]:
            bid_price, bid_size = heapq.heappop(self.bids)
            ask_price, ask_size = heapq.heappop(self.asks)
            qty = min(bid_size, ask_size)
            trades.append((ask_price, qty))
        return trades

    def best_bid_ask(self):
        bb = -self.bids[0][0] if self.bids else None
        ba = self.asks[0][0] if self.asks else None
        return bb, ba
