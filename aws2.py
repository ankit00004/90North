import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Retrieve the file content and metadata from the event
    # Base64-encoded content of the file
    file_content = event.get('file_content')
    bucket_name = event.get('bucket_name')
    file_name = event.get('file_name')

    # Validate input
    if not file_content or not bucket_name or not file_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing file content, bucket name or file name')
        }

    try:
        # Decode the base64-encoded file content
        file_data = base64.b64decode(file_content)

        # Upload the file to the specified S3 bucket
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_data,
            ContentType='application/pdf'  # Assuming the file is a PDF
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully uploaded {file_name} to {bucket_name}')
        }
    except (NoCredentialsError, PartialCredentialsError):
        return {
            'statusCode': 500,
            'body': json.dumps('Error: AWS credentials are missing or incorrect.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
