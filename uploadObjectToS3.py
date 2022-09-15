import boto3

s3_resource = boto3.client("s3")

s3_resource.upload_file(
    Filename = "uploadMe.txt",
    Bucket = "kubelabs",
    Key = "newTxtName.txt"
)