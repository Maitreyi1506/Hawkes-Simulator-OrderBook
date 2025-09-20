# Hawkes-Simulator-OrderBook

# Order Book & Hawkes Simulation

This repo explores **market microstructure** by simulating a **limit order book (LOB)** and modeling order arrivals with **Hawkes processes**. It also implements simple trading strategies (e.g., naive market-making) on synthetic LOB data.

## Features
- **Limit Order Book (LOB) Simulator**
  - Bid/ask queues
  - Matching engine
  - Spread & depth tracking
- **Hawkes Process Arrival Model**
  - Simulate clustered order arrivals via Ogata thinning
  - Compare vs homogeneous Poisson arrivals
- **Strategy Backtests**
  - Simple market-making strategy
  - Naive taker/sniping strategy
  - Track PnL and spread capture
