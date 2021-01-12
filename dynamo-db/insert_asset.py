import boto3
from boto3 import dynamodb
from boto3.session import Session

dynamodb_session = Session(profile_name='TradeTrack')
dynamodb = dynamodb_session.resource('dynamodb', region_name='eu-west-2')
table=dynamodb.Table('assets')

with table.batch_writer() as batch:
    batch.put_item(Item={"id": 2, "ticker": "MSFT",
        "class": "stock", "name": "Microsoft", "quantity": 3})
        