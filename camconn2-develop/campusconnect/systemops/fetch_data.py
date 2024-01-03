import os
import json
from django.conf import settings
from boto3 import client
import boto3

AWS_ACCESS_KEY_ID       = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY   = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME             = 'campuslink-test'


## FAQ data
def fetch_data_faq(product_line):
    s3 = boto3.client('s3',
                     aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                    )

    # Fetch the file object
    FILE_TO_READ = 'media/static-data/faq/product/' + product_line.lower() + '.json'
    file_object = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_TO_READ)
    
    # Read the data from the file object
    # file_data = file_object['Body'].read().decode('utf-8')
    data = json.load(file_object['Body'])
    df = [i for i in data if i['product_line']==product_line]
    da = [i for i in df[0]['ques_ans']]
    return da


## Target audiances
def fetch_data_ta(product_line):
    s3 = boto3.client('s3',
                     aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                    )

    # Define the S3 bucket and file path
    bucket_name = 'campuslink-test'
    file_path = 'media/static-data/faq/target-audiances/ta.json'

    # Retrieve the JSON file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_path)

    # Load the contents of the file as a JSON object
    json_data = json.loads(response['Body'].read())
    json_data = [i['groups'] for i in json_data if i['product_line'] == product_line ]
    json_data = [i for i in json_data[0]]
    
    # Access the JSON data
    # print(json_data)
    return json_data


## Impact Factors
def fetch_data_impfact(product_line):
    s3 = boto3.client('s3',
                     aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                    )

    # Define the S3 bucket and file path
    bucket_name = 'campuslink-test'
    file_path = 'media/static-data/faq/impact-factors/factor-values.json'

    # Retrieve the JSON file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_path)

    # Load the contents of the file as a JSON object
    json_data = json.loads(response['Body'].read())
    json_data = [i['groups'] for i in json_data if i['product_line'] == product_line ]
    json_data = [i for i in json_data[0]]
    
    # Access the JSON data
    # print(json_data)
    return json_data


# USVISA_LIST
visatypes_path = settings.BASE_DIR+"/apiv1/data/"
try:
    with open(visatypes_path+'visa_types.json') as json_file:
        json_data = json.load(json_file)
        # print(json_data)
        USVISA_LIST = json_data
        # print(*USVISA_LIST, sep="\n")
    # USVISA_LIST = []
except IOError:
    print("File Not found")
