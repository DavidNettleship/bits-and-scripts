import requests
import json

response = requests.get('https://api.alternative.me/v1/global/')

#Crypto Fear and Greed Index
fg = (response.json())

with open('fg.json', 'w') as outfile:
                json.dump(fg, outfile)

#AlphaVantage Test
key = ""
stonks = "V:FB:ABBV:RELX"

for stock in stonks.split(":"):
        response_av = requests.get('https://www.alphavantage.co/query?function=OVERVIEW&symbol='+stock+'&apikey='+key)
        data = (response_av.json())

        with open(stock +'.json', 'w') as outfile:
                json.dump(data, outfile)

#CoinLayer API
c_key = ""
crypto = "BTC"

response_av = requests.get('http://api.coinlayer.com/live?access_key='+c_key)
datac = (response_av.json())
with open(crypto +'.json', 'w') as outfile:
               json.dump(datac, outfile)
