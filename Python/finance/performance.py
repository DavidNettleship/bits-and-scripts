import yfinance as yf
import numpy as np


def cagr(data,n):
    df = data.copy()
    df['daily_return'] = df['Adj Close'].pct_change()
    df['cm_return'] = (1+df['daily_return']).cumprod()
    cagr = (df['cm_return'][-1])**(1/n) - 1
    return cagr


def volatility(data):
    df = data.copy()
    df["daily_ret"] = data["Adj Close"].pct_change()
    vol = df["daily_ret"].std() * np.sqrt(len(data))
    return vol


def sharpe(data,rf,n):
    df = data.copy()
    sr = (cagr(df,n) - rf)/volatility(df)
    return sr
 

def max_drawdown(data):
    df = data.copy()
    df["daily_return"] = data["Adj Close"].pct_change()
    df['cm_return'] = (1+df['daily_return']).cumprod()
    df['rolling_max'] = df['cm_return'].cummax()
    df['drawdown'] = df['rolling_max'] - df['cm_return']
    df['drawdown_pct'] = df['drawdown']/df['rolling_max']
    mdd = df['drawdown_pct'].max()
    return mdd


def calmar(data):
    df = data.copy()
    clm = cagr(data,n)/max_drawdown(data)
    return clm


n = 2
rf = 0.022 #2.2%

ticker = "BTC-USD"
data = yf.download(ticker, period=str(n)+"y")

data["Adj Close"].plot()


returns = cagr(data,n)
vv = volatility(data)
sharpe_df = sharpe(data,rf,n)
max_dd = max_drawdown(data)
calmar_v = calmar(data)
