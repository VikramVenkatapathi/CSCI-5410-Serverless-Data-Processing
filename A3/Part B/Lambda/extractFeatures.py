import json
import re
import boto3

def lambda_handler(event, context):
    # Retrieve the S3 event information
    records = event['Records']
    for record in records:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        """
            Boto3 - Amazon Simple Storage Service (S3) API Documentation
            Reference: `Boto3 - Amazon S3 API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_
        """

        # Read the contents of the file from S3
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read().decode('utf-8')
        
        """
            Python Standard Library - re (Regular Expression) module
            Reference: `Python re (Regular Expression) module <https://docs.python.org/3/library/re.html>`_
        """

        # Extract words starting with a capital letter
        capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', file_content)
        
        # Extract all caps words
        all_caps_words = re.findall(r'\b[A-Z]+\b', file_content)
        
        # Create a dictionary to store the named entities and their counts
        named_entities = {}
        
        # Count the occurrences of each word
        for word in capital_words + all_caps_words:
            named_entities[word] = named_entities.get(word, 0) + 1
        
        # Remove the file extension from the key
        file_name = key.split('.')[0]
        
        # Create the JSON object with the key as the file name and the named entities dictionary as the value
        result = {f"{file_name}ne": named_entities}
        
        # Convert the result to a JSON string
        named_entities_json = json.dumps(result)
        
        destination_s3_bucket = "tags-b00936916"

        # Upload the JSON to the tags-b00936916 bucket
        s3_client.put_object(Bucket=destination_s3_bucket, Key=f"{file_name}ne.txt", Body=named_entities_json)

    
    return {
        'statusCode': 200,
        'body': json.dumps('Named entities extracted successfully.')
    }


"""
All references:
    Python Standard Library - re (Regular Expression) module
    Reference: `Python re (Regular Expression) module <https://docs.python.org/3/library/re.html>`_

    Boto3 - Amazon Simple Storage Service (S3) API Documentation
    Reference: `Boto3 - Amazon S3 API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_

"""