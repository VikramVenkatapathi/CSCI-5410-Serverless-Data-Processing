import json
import boto3
import random

# Sample data lists
car_types = ["Compact", "Mid-size Sedan", "SUV", "Luxury"]
car_accessories = ["GPS", "Camera", "Sun shades", "Vehicle Seat Cover"]
client_addresses = ["123 Main St", "456 Elm St", "789 Oak St", "1333 South park st"]

def lambda_handler(event, context):

    """
        W3schools - Python Random Module Documentation
        Reference: `W3schools - Python Random Module <https://www.w3schools.com/python/module_random.asp>`_
    """
    # Generate a single message by combining data from all three lists
    order_details = {
        "type": "ORDER",
        "data": {
            "CAR_TYPE": random.choice(car_types),
            "CAR_ACCESSORY": random.choice(car_accessories),
            "CLIENT_ADDRESS": random.choice(client_addresses)
        }
    }

    # Publish the combined message to the SNS topic
    sns_topic_arn = "arn:aws:sns:us-east-1:000966082997:SendOrderDetailsToSQS"
    publish_to_sns(sns_topic_arn, order_details)
    
    print(order_details)
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to SNS topic=SendOrderDetailsToSQS!')
    }

def publish_to_sns(topic_arn, message):

    """
        Boto3 - Amazon Amazon Simple Notification Service (SNS) Documentation
        Reference: `Boto3 - Amazon SNS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html>`_
    """
    sns_client = boto3.client('sns')

    sns_client.publish(
        TopicArn=topic_arn,
        Message=json.dumps(message)
    )

"""
All references:
    Boto3 - Amazon Amazon Simple Notification Service (SNS) Documentation
    Reference: `Boto3 - Amazon SNS API <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html>`_

    W3schools - Python Random Module Documentation
    Reference: `W3schools - Python Random Module <https://www.w3schools.com/python/module_random.asp>`_
    
"""
