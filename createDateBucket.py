import boto3

s3_resource = boto3.client("s3")

# For loop to go thru every bucket and get it's creation date
for bucket in s3_resource.list_buckets()["Buckets"]:
    creationDate = bucket["CreationDate"]
    # You can also do some formating of the date and time
    print("-----------------------")
    print("Formated date and time:")
    formatedCreationDate = creationDate.strftime("Date: %d-%m-%y // Time: %H:%M:%S")
    print(formatedCreationDate)
