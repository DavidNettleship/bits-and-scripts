import boto3
from boto3.dynamodb.conditions import Key
import requests
import yfinance as yf
import pandas as pd

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    table = client.Table("assets")

    #get list of assets from DynamoDB
    assets = table.scan(FilterExpression=Key('id').gt(-1))

    data = []
    currency = 'GBP'
    
    #Fetch current prices
    for item in assets['Items']:
    
        #coingecko api
        if item['class']=='crypto':
            ticker = item['ticker']
            req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+ item['api_name'] + '&vs_currencies=' + currency)
            req = pd.DataFrame.from_dict(req.json()) 
            rq=req.copy()
            rq['ticker']=ticker
            rq['type']=item['class']
            rq['quant']=item['quantity']
            data.append(rq.to_json(orient='columns'))

        #yfinance api
        if item['class']=='stock':
            ticker = item['ticker']
            close = yf.download(item['api_name'], period="1d")["Close"]
            cl=close.copy()
            cl['ticker'] = ticker
            cl['type'] = item['class']
            cl['quant']=item['quantity']
            
            #UK stocks
            if item['api_name'][-2:] == '.L':
                cl['price']=round(cl[0]/100,2)

            #US stocks
            else:
                cl['price']=round(cl[0]/1.41,2) #TODO: Make exchange rate dynamic

            data.append(cl.to_json(orient='columns'))

    #Current values
    for dat in data:
        asset = dat.split(",")

        #Get stock price
        if asset[2] == "\"type\":\"stock\"":

            raw_ticker = asset[1].split(":")
            ticker = raw_ticker[1].strip('\"').rstrip('\"')

            raw_quant = asset[3].split(":")
            quant = raw_quant[1]

            raw_price = asset[4].split(":")
            price = raw_price[1].rstrip('}')

            value = round(float(price)*float(quant),2)
            
            print(ticker)
            print(value)
        
        elif asset[2] == "\"type\":{\"gbp\":\"crypto\"}":

            raw_ticker = asset[1].split(":")
            ticker = raw_ticker[2].strip('\"').rstrip('\"}')

            raw_quant = asset[3].split(":")
            quant = raw_quant[2].rstrip('}')

            raw_price = asset[0].split(":")
            price = raw_price[2].rstrip('}')

            value = round(float(price)*float(quant),2)

            print(ticker)
            print(value)

#for testing
lambda_handler(1,2)
