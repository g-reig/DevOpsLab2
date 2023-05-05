import boto3
import os

def handler(event, context):
    #event = {"threadId": "threadId"}
    id = event.get('queryStringParameters').get("threadId")
    print(id)
    tableName = os.environ['tableName']
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tableName)
    table.load()
    return getItem(table,id)

def getItem(table,key):
    item = table.get_item(Key={'threadId':key})
    return item
