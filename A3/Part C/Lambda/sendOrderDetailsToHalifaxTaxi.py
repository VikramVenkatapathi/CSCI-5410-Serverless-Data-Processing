import json
import boto3

def handler(event, context):
    # Get the SQS queue URL
    queue_url = "https://sqs.us-east-1.amazonaws.com/000966082997/SNStoHalifaxTaxiQueue"

    """
        Boto3 - Amazon Amazon Simple Queue  Service (SQS) Documentation
        Reference: `Boto3 - Amazon SQS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html>`_
    """

    # Create an SQS client
    sqs = boto3.client('sqs')

    # Receive messages from the SQS queue (max 1 message)
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=30, 
        WaitTimeSeconds=0  # Set to 0 for non-blocking receive
    )

    # Check if any messages were received
    if 'Messages' in response:
        # Extract the message
        message = response['Messages'][0]
        body = json.loads(message['Body'])
        order_details = body['Message']
        # print(order_details)
        
        order_details_json = json.loads(order_details)
        
        # Template for the email body
        email_body_template = """Car Type : {car_type}, Car Accessory : {car_accessory}, Client Address : {client_address}"""

        """
            W3schools - Python String format() Method Documentation
            Reference: `W3schools - Python String format() Method <https://www.w3schools.com/python/ref_string_format.asp>`_
        """
        # Replace the placeholders in the email_body template
        email_body = email_body_template.format(
            car_type=order_details_json['data']['CAR_TYPE'],
            car_accessory=order_details_json['data']['CAR_ACCESSORY'],
            client_address=order_details_json['data']['CLIENT_ADDRESS']
        )

        # Publish the message to the SNS topic
        sns_topic_arn = "arn:aws:sns:us-east-1:000966082997:SendOrderDetailsToEmail"
        
        publish_to_sns(sns_topic_arn, email_body)

        # Delete the message from the SQS queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to subscriber')
    }

def publish_to_sns(topic_arn, message):
    # Create an SNS client
    sns = boto3.client('sns')

    """
        Boto3 - Amazon Amazon Simple Notification Service (SNS) Documentation
        Reference: `Boto3 - Amazon SNS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html>`_
    """
    # Publish the message to the SNS topic
    sns.publish(
        TopicArn=topic_arn,
        Subject="Your order details",
        Message=json.dumps(message)
    )

"""
All references:
    Boto3 - Amazon Amazon Simple Notification Service (SNS) Documentation
    Reference: `Boto3 - Amazon SNS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html>`_

    Boto3 - Amazon Amazon Simple Queue  Service (SQS) Documentation
    Reference: `Boto3 - Amazon SQS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html>`_

    W3schools - Python Random Module Documentation
    Reference: `W3schools - Python Random Module <https://www.w3schools.com/python/module_random.asp>`_
    
"""