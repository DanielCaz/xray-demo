import os
import json
import boto3

TABLE_NAME = os.getenv('TABLE_NAME')

ddb = boto3.resource('dynamodb')
table = ddb.Table(TABLE_NAME)


def lambda_handler(event, context):
    body = json.loads(event['body'])

    table.put_item(Item={
        'id': body['id'],
        'name': body['name'],
    })

    return build_response(200, {'message': 'Operation successful'})


def build_response(status_code, body):
    return {
        'headers': {
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*',
        },
        'statusCode': status_code,
        'body': json.dumps(body),
    }
