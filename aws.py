

import os
import boto3 
import pandas as pd


client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = 'ap-south-1'
)
    
clientResponse = client.list_buckets() 

print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


obj = client.get_object(
    Bucket = 'cyber-mads',
    Key = 'y_test_amex.csv'
)

obj2 = client.get_object(
    Bucket = 'cyber-mads',
    Key = 'sample_upload.csv'
)

print(obj['Body'])
print(obj2['Body'])

# for body in obj['Body']: 
# 	print(body)

data = pd.read_csv(obj['Body'])
# data = aws.s3.read_csv(path="s3://cyber-mads/x_test_amex.csv")
