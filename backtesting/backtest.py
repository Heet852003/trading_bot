import backtrader as bt

class MovingAverageStrategy(bt.Strategy):
    params = (('short_window', 40), ('long_window', 100),)

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.short_mavg = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.short_window)
        self.long_mavg = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.long_window)
        self.crossover = bt.indicators.CrossOver(self.short_mavg, self.long_mavg)

    def next(self):
        if self.crossover > 0:
            self.buy()
        elif self.crossover < 0:
            self.sell()

if __name__ == "__main__":
    import data.fetch_data as fetch
    from datetime import datetime

    cerebro = bt.Cerebro()

    data = fetch.fetch_data("AAPL", "2020-01-01", "2023-01-01")
    data_feed = bt.feeds.PandasData(dataname=data)

    cerebro.adddata(data_feed)
    cerebro.addstrategy(MovingAverageStrategy)

    cerebro.run()
    cerebro.plot()
