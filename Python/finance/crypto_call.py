import yfinance as yf
import pandas as pd


tickers = ["BTC-GBP","ETH-GBP"]
close = pd.DataFrame()
data = {}

for ticker in tickers:
    close[ticker] = yf.download(ticker, period="1mo")["Close"]
    data[ticker] = yf.download(ticker, period="7d", interval="1m")

