import yfinance as yf
import numpy as np
from stocktrends import Renko


#MACD
def macd(data):
    df = data.copy()
    df['MA_Fast']=df['Adj Close'].ewm(span=12,min_periods=12).mean()
    df['MA_Slow']=df['Adj Close'].ewm(span=26,min_periods=26).mean()
    df['MACD']=df['MA_Fast']-df['MA_Slow']
    df['Signal']=df['MACD'].ewm(span=9,min_periods=9).mean()
    df.drop(columns=['MA_Fast','MA_Slow'], inplace=True)
    df.dropna(inplace=True)
    return df['MACD']


#Bollinger Bands
def bollinger(data,n):
    df = data.copy()
    df['MA']=df['Adj Close'].rolling(n).mean()
    df['bb_up']=df['MA'] + df['MA'].rolling(n).std()
    df['bb_down']=df['MA'] - df['MA'].rolling(n).std()
    df['bb_range']=df['bb_up']-df['bb_down']
    df['bb_mid']=df['bb_up']-(df['bb_range']/2)
    df.dropna(inplace=True)
    return df


#ATR
def atr(data,n):
    df = data.copy()
    df['H-L']=abs(df['High']-df['Low'])
    df['H-PC']=abs(df['High']-df['Adj Close'].shift(1))
    df['L-PC']=abs(df['Low']-df['Adj Close'].shift(1))
    df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1,skipna=False)
    df['ATR']=df['TR'].rolling(n).mean()
    df = df.drop(columns=['H-L','H-PC','L-PC'],axis=1)
    df.dropna(inplace=True)
    return df


#RSI
def rsi(data,n):
    df = data.copy()
    df['delta']=df['Adj Close'] - df['Adj Close'].shift(1)
    df['gain']=np.where(df['delta']>=0,df['delta'],0)
    df['loss']=np.where(df['delta']<0,abs(df['delta']),0)
    avg_gain = []
    avg_loss = []
    gain = df['gain'].tolist()
    loss = df['loss'].tolist()
    
    for i in range(len(df)):
        if i < n:
            avg_gain.append(np.NaN)
            avg_loss.append(np.NaN)
        elif i == n:
            avg_gain.append(df['gain'].rolling(n).mean().tolist()[n])
            avg_loss.append(df['loss'].rolling(n).mean().tolist()[n])
        elif i > n:
            avg_gain.append(((n-1)*avg_gain[i-1]+ gain[i])/n)
            avg_loss.append(((n-1)*avg_loss[i-1]+ loss[i])/n)
    
    df['avg_gain']=np.array(avg_gain)            
    df['avg_loss']=np.array(avg_loss) 
    df['RS'] = df['avg_gain']/df['avg_loss']
    df['RSI'] = 100 - (100/(1+df['RS']))
    df.dropna(inplace=True)
    return df['RSI']


#OBV
def obv(data):
    df = data.copy()
    df['daily_ret'] = df['Adj Close'].pct_change()
    df['direction'] = np.where(df['daily_ret']>=0,1,-1)
    df['direction'][0] = 0
    df['vol_adj'] = df['Volume'] * df['direction']
    df['obv'] = df['vol_adj'].cumsum()
    return df['obv']


#Renko
def renko(data):
    df = data.copy()
    df.reset_index(inplace=True)
    df = df.iloc[:,[0,1,2,3,5,6]]
    df.rename(columns = {"Date" : "date", "High" : "high","Low" : "low", "Open" : "open","Adj Close" : "close", "Volume" : "volume"}, inplace = True)
    dfr = Renko(df)
    print(dfr)
    dfr.brick_size = round(atr(data,120)["ATR"][-1],0)
    renko_df = dfr.get_ohlc_data()
    return renko_df


#main
ticker = "BTC-USD"
data = yf.download(ticker, period="2y")
    
macd_df = macd(data)
atr_df = atr(data,20)
bol_df = bollinger(data,20)
rsi_df = rsi(data,20)
obv_df = obv(data)
renko_df = renko(data)

#bollinger bands plot
plot=bol_df.iloc[:,[-4,-3,-2]].plot()
