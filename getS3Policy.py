import boto3

s3_resource = boto3.client("s3")
kubelabs_policy = s3_resource.get_bucket_policy(Bucket="kubelabs")['Policy']

print(kubelabs_policy)
