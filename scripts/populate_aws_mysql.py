
import json
import boto3
import string
import pymysql
from datetime import datetime

now = datetime.now()
formatted_date = str(now.strftime('%Y-%m-%d'))

def aws_sql_connect(output):

  """
  Creates MySQL table in aws and populate the table with message received from SQS
  after masking user sensitive fields

  input : masked list of messages received from SQS
  output : MySQL table populated with the data

  """

    host_link = aws_host_link
    username = username
    pw = pwd
    database_name = database_name

    db = pymysql.connect(user=username, password=pw, host=host_link, port=3306)

    cursor = db.cursor()

    sql_create_table = '''create database SQS_user_data'''
    cursor.execute(sql_create_table)
    cursor.connection.commit()

    print("Database created !!")

    sql_use_this_database = '''use SQS_user_data'''
    cursor.execute(sql_use_this_database)

    print("Using given database !!")


    sql_create_table = '''

    CREATE TABLE IF NOT EXISTS user_login (
    user_id             varchar(128),
    device_type         varchar(32),
    masked_ip           varchar(256),
    masked_device_id    varchar(256),
    locale              varchar(32),
    app_version         varchar(32),
    create_date         date )
    '''
    cursor.execute(sql_create_table)
    print("Table created in Database !!")


    formatted_date = str(now.strftime('%Y-%m-%d'))

    for out in output:
        cursor.execute("""
    INSERT INTO 
    user_login    
    VALUES
        ( %s , %s , %s , %s , %s , %s , %s )""",
                       (out['user_id'], out['device_type'], out['ip'], out['device_id'],
                        out['locale'], out['app_version'], formatted_date)
                       )
    print("Data inserted into MySQL Table !!")


    sql = '''select * from user_login'''
    cursor.execute(sql)
    print(cursor.fetchall())
