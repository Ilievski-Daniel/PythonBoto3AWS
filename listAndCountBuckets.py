import boto3

resource = boto3.resource("s3")

# Get all the S3 Buckets Names
for bucket in resource.buckets.all():
    print(bucket.name)

# How to count the number of S3 Buckets
numberOfBuckets = len(list(resource.buckets.all()))
print("There are: " + str(numberOfBuckets) + " S3 Buckets")