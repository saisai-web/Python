import json
import boto3
import os
import datetime
import botocore


from botocore.exceptions import ClientError

def handler(event, context):
    print(event)
    try:
        environment = os.environ.get('JOB_TEMPLATE')
        
        print(environment)

        eventtypename=event['Records'][0]['eventName']
            responses = event['Records'][0]['dynamodb']['NewImage']
            tenantId=responses['tenantId']['S']
        
        if eventtypename in 'REMOVE' or eventtypename in 'MODIFY':
            oldimage = event['Records'][0]['dynamodb']['OldImage']
        s3 = boto3.client('s3')
        s3client = boto3.resource('s3')
        client = s3client.meta.client
        
        buckets = s3.list_buckets()['Buckets']
            Bucket=bucket['Name']
                    if eventtypename in 'INSERT':
                    
					elif eventtypename in 'MODIFY':
                        
                    elif eventtypename in 'REMOVE':
                    
    except Exception as e:
        print(e) 

