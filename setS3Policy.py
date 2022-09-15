import boto3
import json

s3_resource = boto3.client("s3")
bucket_policy = {
"Version": "2012-10-17",
"Statement": [
{
"Sid": "Statement1",
"Effect": "Allow",
"Principal": "*",
"Action": "s3:GetObject",
"Resource": "arn:aws:s3:::kubelabs/*"
}
]
}
bucket_policy = json.dumps(bucket_policy)
s3_resource.put_bucket_policy(Bucket="kubelabs",Policy=bucket_policy)