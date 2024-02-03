import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="rxs-101623", Key="text_test_string.txt", Body="Hey this is a string",ContentType="text/plain")
