import logging
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3', region_name = 'eu-west-1')
location = {'LocationConstraint': 'eu-west-1'}
client.create_bucket(Bucket='gabrielbucket911012',
                       CreateBucketConfiguration=location)


#List existing buckets

listOfBuckets = client.list_buckets()

print(listOfBuckets['Buckets'])


#Uploading Files

def upload_files(file_name,bucket,object_name= None , args =None):
    if object_name is None:
        object_name = file_name

    response = client.upload_file(file_name, bucket, object_name, ExtraArgs = args)
    print(response)

#Lets upload file

upload_files('C://Users//Asus//Desktop//DS//DockerFix.txt','gabrielbucket911012')

import glob

files = glob.glob('C://Users//Asus//Desktop//DS//*')
print(files)
for file in files:
    upload_files(file, 'gabrielbucket911012')
    print('uploaded', file)

#Download files from s3


s3 = boto3.resource('s3')
print(list(s3.buckets.all()))  #This and below command does the same, more info comes with client
client.list_buckets()

bucket = s3.Bucket('gabrielbucket911012')
files = list(bucket.objects.all())
for file in files:
    #dn = file.split('')
    client.download_file('gabrielbucket911012', file.key, file.key)


#Lets set bucket policy

import json

bucket_name = 'gabrielbucket911012'
bucket_policy = {

    "Version" : "2012-10-17",
    "Statement" : [
        {
            "Sid":"PublicRead",
            "Effect":"Allow",
            "Principal": "*",
            "Action":["s3:GetObject","s3.GetObjectVersion"],
            "Resource":["arn:aws:s3:::gabrielbucket911012/"]
        }
    ]


  }

bucket_policy = json.dumps(bucket_policy)

client.put_bucket_policy(Bucket = bucket_name, Policy = bucket_policy)
