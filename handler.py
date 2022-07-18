import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('poc2_customer_table')

def crud_operations(event, context):
    stage = context['function_name'].split('-')[0]
    print("Current stage", stage)
    if event['httpMethod'] == "PUT":
        input_data = event['body']
        final_data = json.loads(input_data)
        table.put_item(Item=final_data)
        return {'statusCode': 200,'body': 'Items successfully stored in the new table'}

    elif event['httpMethod'] == "DELETE":
        input_data = event['body']
        final_data = json.loads(input_data)
        Customer_id = final_data['Customer_id']
        response = table.delete_item(Key={'Customer_id': Customer_id})
        return{'statusCode': 200, 'body': "items deleted successfully"}

    elif event['httpMethod'] == "POST":
        input_data = json.loads(event['body'])
        Customer_id = input_data['Customer_id']
        response = table.get_item(Key={'Customer_id': Customer_id})
        table_data = response['Item']
        for i in input_data:
            if table_data[i] == input_data[i]:
                pass
            else:
                table_data[i] = input_data[i]
        table.put_item(Item=table_data)
        return{'statusCode' : 200, 'body' : 'item successfully updated'}

    elif event['httpMethod'] == "GET":
        Customer_id = event['queryStringParameters']['Customer_id']
        response = table.get_item(Key={'Customer_id': Customer_id})
        return{'statusCode': 200,'body': json.dumps(response['Item'])}

    else:
        return {'statusCode': 200,'body': 'You choose other than CRUD operations. please check your method '
        }
