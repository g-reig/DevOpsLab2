import boto3
import os

def handler(event, context):
    tableName = os.environ['tableName']
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tableName)
    table.load()
    return scanItems(table,'threadId')

def scanItems(table,projection):
    return table.scan(ProjectionExpression=projection)
