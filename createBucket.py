import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            # If region is none the default one is N.Virgina (eu-east-1)
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # We only need name and region to be able to create a S3 Bucket
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    # Here we simply catch the error if something goes wrong
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket("kubelabstesting")