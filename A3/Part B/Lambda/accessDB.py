import json
import boto3

def lambda_handler(event, context):
    # Retrieve the S3 event information
    records = event['Records']
    for record in records:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Check if the file is in the format "001ne.txt"
        if key.endswith("ne.txt"):
            """
                Boto3 - Amazon Simple Storage Service (S3) API Documentation
                Reference: `Boto3 - Amazon S3 API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_
            """
            # Read the contents of the file from S3            
            s3_client = boto3.client('s3')

            response = s3_client.get_object(Bucket=bucket, Key=key)
            file_content = response['Body'].read().decode('utf-8')
            
            # Convert the JSON content to a dictionary
            named_entities = json.loads(file_content)
            
            # Get the file name from the key (e.g., "001ne.txt" -> "001ne")
            file_name = key.split('.')[0]
            
            """
                Boto3 - Amazon DynamoDB API Documentation
                Reference: `Boto3 - Amazon DynamoDB API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html>`_
            """
            # Update the DynamoDB table with the named entities
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('Entities')
            
            for entity, count in named_entities[file_name].items():
                # Convert the count to an integer before updating the table
                count = int(count)
                # Update the table with the named entity and its count
                table.update_item(
                    Key={'entity_name': entity},
                    UpdateExpression='SET frequency = if_not_exists(frequency, :zero) + :val',
                    ExpressionAttributeValues={':zero': 0, ':val': count}
                )
                
    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDB table updated successfully.')
    }



"""
All references:
    Boto3 - Amazon Simple Storage Service (S3) API Documentation
    Reference: `Boto3 - Amazon S3 API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_

    Boto3 - Amazon DynamoDB API Documentation
    Reference: `Boto3 - Amazon DynamoDB API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html>`_
"""
