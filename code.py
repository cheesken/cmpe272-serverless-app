import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentRecords')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # C = Create
        student = json.loads(event['body'])
            
        if 'student_id' not in student:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'student_id is missing!!!'})
            }
            
        table.put_item(Item=student)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Student record added successfully', 'student': student})
        }
    elif event['httpMethod'] == 'GET':
        # R = Read
        if not event.get('queryStringParameters') or not event['queryStringParameters'].get('student_id'):
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'student_id query parameter is missing!!'})
                }
            
        student_id = event['queryStringParameters']['student_id']
        response = table.get_item(Key={'student_id': student_id})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'oopsie no student record found'})
            }
            
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    elif event['httpMethod'] == 'PATCH':
        # U = Update
        if not event.get('body'):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Bruh... No body? Really??'})
            }

        student_data = json.loads(event['body'])
            
        if 'student_id' not in student_data:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'student_id is missing!!'})
            }
            
        table.put_item(Item=student_data)
            
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Student record updated successfully', 'student': student_data})
        }
    elif event['httpMethod'] == 'DELETE':
        # D = Delete
            if not event.get('queryStringParameters') or not event['queryStringParameters'].get('student_id'):
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'student_id query parameter is missing!!'})
                }
            
            student_id = event['queryStringParameters']['student_id']
            
            response = table.get_item(Key={'student_id': student_id})
            if 'Item' not in response:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'error': 'oopsie no student record found'})
                }
            
            table.delete_item(Key={'student_id': student_id})
            
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Student record deleted successfully'})
            }
