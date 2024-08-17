import streamlit as st
import pandas as pd
from trading_bot.data.fetch_data import fetch_data
from trading_bot.strategies.moving_average import moving_average_strategy
from trading_bot.backtesting.backtest import MovingAverageStrategy
import backtrader as bt
import matplotlib.pyplot as plt

# Set up Streamlit page config
st.set_page_config(page_title="Algorithmic Trading Bot", layout="wide")

# UI Components
st.title("Algorithmic Trading Bot")
st.write("A modern and intuitive interface to test your trading strategies with real-time data.")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))

if st.button("Fetch Data"):
    data = fetch_data(ticker, start_date, end_date)
    st.write("### Stock Data")
    st.dataframe(data.head())

    st.write("### Price Chart")
    st.line_chart(data['Close'])

    st.write("### Moving Average Strategy")
    signals = moving_average_strategy(data)
    st.line_chart(signals[['short_mavg', 'long_mavg']])

    if st.button("Run Backtest"):
        cerebro = bt.Cerebro()
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        cerebro.addstrategy(MovingAverageStrategy)
        st.write("### Backtest Results")
        cerebro.run()
        cerebro.plot(style='bar')
