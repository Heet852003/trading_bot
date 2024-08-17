from data.fetch_data import fetch_data
from strategies.moving_average import moving_average_strategy
from backtesting.backtest import MovingAverageStrategy
import backtrader as bt
import matplotlib.pyplot as plt

def main():
    # Step 1: Fetch Stock Data
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    data = fetch_data(ticker, start_date, end_date)
    
    # Step 2: Apply Trading Strategy
    signals = moving_average_strategy(data)
    
    # Step 3: Backtest Strategy
    cerebro = bt.Cerebro()
    data_feed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(data_feed)
    cerebro.addstrategy(MovingAverageStrategy)
    cerebro.run()
    
    # Step 4: Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label="Price")
    plt.plot(signals.index, signals['short_mavg'], label="Short Moving Average")
    plt.plot(signals.index, signals['long_mavg'], label="Long Moving Average")
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
