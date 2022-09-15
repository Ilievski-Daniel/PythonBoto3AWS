import boto3
import os
import glob

# Files location
cwd = os.getcwd()+"/UploadMultiple/"
print(cwd)
# The actual files
files = glob.glob(cwd+"*.txt")

# For loop for uploading files
for file in files:
    s3_resource = boto3.client("s3")

    s3_resource.upload_file(
        Filename = file,
        Bucket = "kubelabs",
        Key = file.split("/")[-1]
    )