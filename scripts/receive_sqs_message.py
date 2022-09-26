import json
import boto3
import string
import pymysql
from datetime import datetime

# create sqs client
sqs_client = boto3.client("sqs")

#  create sqs queue named login queue
QUEUE_NAME = "login-queue"
queue_url = sqs.create_queue(QueueName=QUEUE_NAME)["QueueUrl"]

# create empty list to append the received message
unmasked_json = []





def receive_messages():

    """
    receives message sent to the sqs_queue
    input : Queue-Url where message was sent
    output : Received messages appended to list
    
    """

    for i in range(0, 100):

        response = sqs_client.receive_message(QueueUrl=queue_url)

        msg_body = response['Messages'][0]['Body']

        json_body = json.loads(msg_body)

        unmasked_json.append(json_body)

    return unmasked_json
