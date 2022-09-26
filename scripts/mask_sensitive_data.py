import json
import boto3
import string
import pymysql
from datetime import datetime


def transform(unmasked):
    """
    Masking function to mask user_id and user_device_id in a way that 
    duplicate values could be identified.
    This function will substitute integers with alphabets
    
    input  : Received messages list from SQS queue
    output : List of messages with masked id and device_id
    
    """

    masking = dict()

    for i in range(0, 10):
        masking[i] = string.ascii_lowercase[i]

    for records in unmasked:
        ip = records['ip']
        device_id = records['device_id']
        list_ip = list(ip)
        list_id = list(device_id)

        # masking ip

        for i, char in enumerate(list_ip):
            if char == ".":
                list_ip[i] = char
            else:
                list_ip[i] = masking[int(char)]

        masked_ip = "".join(list_ip)
        records['ip'] = masked_ip

        # masking device_id

        for i, char in enumerate(list_id):
            if char == "-":
                list_id[i] = char
            else:
                list_id[i] = masking[int(char)]

        masked_id = "".join(list_id)
        records['device_id'] = masked_id

    return unmasked
