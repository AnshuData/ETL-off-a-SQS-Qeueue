import json
import boto3
import string
import pymysql
from datetime import datetime

from scripts.create_and_send_message_to_sqsqueue import send_messages
from scripts.receive_sqs_message import receive_messages
from scripts.mask_sensitive_data import transform
from scripts.populate_aws_mysql import aws_sql_connect

def main():
"""
Application that creates SQS queue, send data to SQS queue,
reads such data from an AWS SQS Qeueue, transform that data, 
then write to a AWS MySQL database
"""

    send_messages()
    receive_messages()
    masked_json = transform(unmasked_json)
    aws_sql_connect(masked_json)


if __name__ == "__main__":
    main()
