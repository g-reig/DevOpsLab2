import boto3
import os
from uuid import uuid4

def handler(event, context):
    # event = {"threadId": "threadId","author": "author", "message", "message"}
    threadId = event.get('threadId', None) 
    author = event.get('author', 'Anon')
    message = event.get('message')
    tableName = os.environ['tableName']
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tableName)
    table.load()
    if not threadId:
        threadId = str(uuid4())
        item = {'threadId': threadId, 'threadMessages': [
                        {'message': message, 'author': author}]}
        putItem(table, item)
    else:
        updateItems(table,threadId,{'message':message,'author':author})
    return 

def updateItems(table,key,value):
    return table.update_item(Key={'threadId':key},
                      UpdateExpression='set threadMessages = list_append(threadMessages,:val)',
                      ExpressionAttributeValues={':val':[value]},
                      ReturnValues='UPDATED_NEW')

def putItem(table, item):
    table.put_item(Item=item)