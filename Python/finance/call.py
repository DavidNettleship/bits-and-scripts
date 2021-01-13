import yfinance as yf
import pandas as pd


tickers = ["MSFT", "AMZN", "FB", "GOOG", "REL.L"]
close = pd.DataFrame()
data = {}

for ticker in tickers:
    close[ticker] = yf.download(ticker, period="3mo")["Close"]
    data[ticker] = yf.download(ticker, period="3mo")

