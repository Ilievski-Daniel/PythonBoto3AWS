import boto3

s3_resource = boto3.client("s3")

objects = s3_resource.list_objects(Bucket="kubelabs")['Contents']

for object in objects:
    # object - will contain the information 
    # From here we can do myltiple things, what information do we need?
    # Lets say the name if the file
    print("Object name: " + object['Key'])
    # Or maybe the Size?
    print("Object size: " + str(object['Size']))
    print("-----------------------------------")