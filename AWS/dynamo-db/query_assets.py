import boto3
from boto3 import dynamodb
from boto3.session import Session
from boto3.dynamodb.conditions import Key

dynamodb_session = Session(profile_name='TradeTrack')
dynamodb = dynamodb_session.resource('dynamodb', region_name='eu-west-2')
table=dynamodb.Table('assets')

response = table.query(KeyConditionExpression=Key('id').eq(0))

#print(response)

print("Query")
for item in response['Items']:
    print(item)
    
print("Scan")
scan1 = table.scan(FilterExpression=Key('class').eq("stock"))
scan2 = table.scan(FilterExpression=Key('id').gt(-1))

print("Scan 1")
for item in scan1['Items']:
    print(item)

print("Scan 2")
for item in scan2['Items']:
    print(item)
    