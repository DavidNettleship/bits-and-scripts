import yfinance as yf
import pandas as pd


tickers = ["MSFT", "AMZN", "FB", "GOOG", "LSE.L", "BTC-GBP"]
close = pd.DataFrame()
data = {}

for ticker in tickers:
    close[ticker] = yf.download(ticker, period="1y")["Close"]
    data[ticker] = yf.download(ticker, period="3mo")

#fill NaN values
close.fillna(method='ffill',inplace=True)
mean = close.mean()
deviation = close.std()

#returns
daily_return = close.pct_change()
mean_return = daily_return.mean()
return_deviation = daily_return.std()

#rolling data
rolling_return = daily_return.rolling(window=20, min_periods=1).mean() #20 day simple rolling avg
ema = daily_return.ewm(span=20,min_periods=20).mean() # exponential moving average (20 day ema)
rolling_deviation = daily_return.rolling(window=20, min_periods=1).std() #20 day deviation rolling avg

#visualisations
close.plot()
standardised = (close-close.mean())/close.std()
standardised.plot()

close.plot(subplots=True, layout=(3,2), title = "Example", grid=True)
