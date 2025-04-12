import boto3

# Create an S3 resource
s3 = boto3.resource('s3')

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)

