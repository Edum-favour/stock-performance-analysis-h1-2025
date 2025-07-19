import yfinance as yf
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp500_table = pd.read_html(url)[0]

sp500_table["Symbol"] = sp500_table["Symbol"].str.strip().str.upper()
sp500_table["Security"] = sp500_table["Security"].str.strip()

ticker_name_map = dict(zip(sp500_table["Symbol"], sp500_table["Security"]))
tickers = list(ticker_name_map.keys())

return tickers, ticker_name_map