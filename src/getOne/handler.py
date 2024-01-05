import os
import json
import boto3

TABLE_NAME = os.getenv('TABLE_NAME')

ddb = boto3.resource('dynamodb')
table = ddb.Table(TABLE_NAME)


def lambda_handler(event, context):
    id = event['pathParameters']['id']

    response = table.get_item(Key={'id': id})

    item = response['Item']

    return build_response(200, item)


def build_response(status_code, body):
    return {
        'headers': {
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*',
        },
        'statusCode': status_code,
        'body': json.dumps(body),
    }
