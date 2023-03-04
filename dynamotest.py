import boto3

def getItem(table,key):
    item = table.get_item(Key={'threadId':key})
    return item

def putItem(table,item):
    table.put_item(Item=item)

def scanItems(table,projection):
    return table.scan(ProjectionExpression=projection)

def updateItems(table,key,value):
    return table.update_item(Key={'threadId':key},
                      UpdateExpression='set threadMessages = list_append(threadMessages,:val)',
                      ExpressionAttributeValues={':val':[value]},
                      ReturnValues='UPDATED_NEW')

tableName = 'message_board'
dynamo = boto3.resource('dynamodb')
table = dynamo.Table(tableName)
table.load()

#print(getItem(table,'1'))
#putItem(table,{'threadId':'2','threadMessages':[{'message':'Hello world!','author':'Groig'}]})
#updateItems(table,'2',{'message':'hola','author':'groig'})
#print(scanItems(table,'threadId'))
