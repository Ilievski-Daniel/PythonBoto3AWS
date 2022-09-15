import boto3
import os
import glob

s3_resource = boto3.client("s3")

objects = s3_resource.list_objects(Bucket="kubelabs")['Contents']

for object in objects:
    s3_resource.delete_object(Bucket="kubelabs", Key=object['Key'])