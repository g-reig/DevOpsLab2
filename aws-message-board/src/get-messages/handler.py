import boto3
import os
import json

def handler(event, context):
    #event = {"id": "id"}
    id = event['id']
    print(id)
    tableName = os.environ['tableName']
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tableName)
    table.load()
    return getItem(table,id)


def getItem(table,key):
    item = table.get_item(Key={'threadId':key})
    return item
