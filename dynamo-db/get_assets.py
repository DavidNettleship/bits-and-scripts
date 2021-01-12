import boto3

session=boto3.Session(profile_name='TradeTrack')
client = session.client('dynamodb', region_name='eu-west-2')
table = "assets"

response = client.list_tables()
print(response)

response = client.get_item(TableName="assets", Key={"id": {"N": "1"}, "ticker": {"S": "BTC"}})
print(response)
