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


def send_messages():

    """
    send json_data to sqs_queue
    We send data in the form of json_file to SQS queue
    For test; we only send 100 data points
    """

    print(f"queue_url: [{queue_url}]")

    with open("./data/sample.json", "r") as f:
        data = json.load(f)

    assert len(data) == 100 # sending only 100 data points for test

    for record in data:
        sqs.send_message(QueueUrl = queue_url, MessageBody=json.dumps(record))
