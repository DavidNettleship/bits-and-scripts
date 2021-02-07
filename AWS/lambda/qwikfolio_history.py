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
    
    for item in assets['Items']:
    
        #coingecko api
        if item['class']=='crypto':
            ticker = item['ticker']
            req = requests.get('https://api.coingecko.com/api/v3/simple/price?ids='+ item['api_name'] + '&vs_currencies=' + currency)
            req = pd.DataFrame.from_dict(req.json()) 
            rq=req.copy()
            rq['ticker']=ticker
            data.append(rq.to_json(orient='columns'))

        #yfinance api
        if item['class']=='stock':
            ticker = item['ticker']
            close = yf.download(item['api_name'], period="1d")["Close"]
            cl=close.copy()
            cl['ticker']=ticker
            cl['price']=cl[0]
            data.append(cl.to_json(orient='columns'))

    for dat in data:
        print(dat)

#for testing
lambda_handler(1,2)
