# 📈 **Algorithmic Trading Bot**

![Python](https://img.shields.io/badge/Python-3.8-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)

---

## 🚀 **Overview**

The **Algorithmic Trading Bot** is a Python-based application that automates trading decisions using quantitative strategies. It features a Moving Average strategy to trade stocks or cryptocurrencies based on historical data. The bot also includes a modern UI built with **Streamlit**, making it easy to visualize trading signals and backtest results interactively.

This bot is designed to help traders analyze the market and automate trades efficiently. Whether you're trading stocks or cryptocurrencies, this bot can save time and reduce manual intervention.

---

## 🔧 **Features**

- 📊 **Fetch Historical Data**: Retrieve stock or cryptocurrency data using the **Yahoo Finance** API.
- 📈 **Moving Average Strategy**: Implement moving average crossover strategies to generate trading signals.
- 🧪 **Backtesting**: Test your trading strategies on historical data to evaluate performance before deploying them.
- 🖥️ **Interactive UI**: A clean, modern UI built with **Streamlit** for visualizing stock data, trading signals, and backtest results.

---

## 💻 **Installation**

### 1. Clone the Repository
    
    git clone https://github.com/Heet852003/trading_bot.git
    cd trading_bot

### 2. Set Up a Virtual Environment :Create and activate a virtual environment
    python -m venv venv
On Windows
 
    python -m venv venv.\venv\Scripts\activate

On macOS/Linux:
  ```bash
  source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages:

   ```bash
pip install -r requirements.txt
```

## 🏃‍♂️ **Usage**

### 1. Run the Bot Locally
To test the bot locally, run the main script:
```bash
python trading_bot.py
```
This will fetch data, apply the strategy, and plot the results using matplotlib.

### 2. Run the Streamlit App
To launch the Streamlit UI, run:
```bash
streamlit run ui/app.py
```
This will start the Streamlit server and open the application in your web browser.

### 3. Deploy on Streamlit Cloud
Push Your Code to GitHub:
```bash
git add .
git commit -m "Initial commit with Streamlit UI"
git push origin master
```
Deploy on Streamlit Cloud:

- Go to Streamlit Cloud and log in.
- Click on "New app" and select your GitHub repository.
- Set the entry point to ui/app.py and deploy.
