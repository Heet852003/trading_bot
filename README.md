# Algorithmic Trading Bot

## Overview

The Algorithmic Trading Bot is a Python-based trading application that leverages quantitative strategies to automate trading decisions. This bot implements a Moving Average strategy to trade stocks or cryptocurrencies based on historical data. The bot features a modern UI built with Streamlit for interactive visualization and testing of trading strategies.

## Features

- **Fetch Historical Data**: Retrieve stock or cryptocurrency data using Yahoo Finance.
- **Apply Moving Average Strategy**: Implement moving average crossover strategies for trading signals.
- **Backtesting**: Test trading strategies on historical data to evaluate performance.
- **Interactive UI**: Use Streamlit to visualize stock data, trading signals, and backtest results.

## Installation

### 1. Clone the Repository

git clone https://github.com/Heet852003/trading_bot.git
cd trading_bot

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:
python -m venv venv

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

### 3. Install Dependencies

Install the required packages:
pip install -r requirements.txt

## Usage

### 1. Run the Bot Locally

To test the bot locally, run:
python trading_bot.py

This will execute the main script, fetching data, applying the strategy, and plotting the results.

### 2. Run the Streamlit App

To use the Streamlit interface, run:
streamlit run ui/app.py

This will start the Streamlit server and open the application in your web browser.

### 3. Deploy on Streamlit Cloud

Push your code to GitHub:

git add .
git commit -m "Initial commit with Streamlit UI"
git push origin master

Deploy on Streamlit Cloud:

Go to Streamlit Cloud and log in.
Click on "New app" and select your GitHub repository.
Set the entry point to ui/app.py and deploy.

## Contribution
Contributions are welcome! Please follow these steps to contribute:

Fork the Repository: Click the "Fork" button on GitHub to create your own copy of the repository.
Create a Branch: Make a new branch for your feature or fix.

git checkout -b feature-branch

Make Your Changes: Implement your changes and test them locally.
Submit a Pull Request: Push your changes to your fork and submit a pull request to the main repository.


## Acknowledgments

Yahoo Finance for providing the stock data.
Backtrader for the backtesting framework.
Streamlit for the interactive UI framework.

## Contact
For any questions or feedback, please contact mehtaheet5@gmail.com.
