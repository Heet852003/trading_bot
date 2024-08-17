import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    data = fetch_data("AAPL", "2020-01-01", "2023-01-01")
    print(data.head())
