import boto3

s3 = boto3.client('s3')

with open("text_test.txt", 'rb') as f:
    s3.put_object(Bucket="rxs-101623", Key="text_test.txt", Body=f,ContentType="text/plain")
