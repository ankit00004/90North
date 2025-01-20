import json


def lambda_handler(event, context):
    # Extract numbers from the event object (assuming the numbers are passed in as JSON parameters)
    num1 = event.get('num1')
    num2 = event.get('num2')

    # Validate input
    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing num1 or num2')
        }

    # Add the numbers
    result = num1 + num2

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
