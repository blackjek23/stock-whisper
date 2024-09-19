import yfinance as yf
import pandas as pd
from datetime import date, timedelta

def download_stocks_data():
    end_date = date.today()
    start_date = end_date - timedelta(days=365)

    with open('stocks.txt', 'r') as f:
        for ticker in f:
            Symbol = ticker.strip()
            df = yf.download(Symbol, start=start_date, end=end_date, interval="1d")
            df.to_csv(f'./DataBase/{Symbol}.csv')

if __name__ == "__main__":
    download_stocks_data()
