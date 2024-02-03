import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "rxs-101623", 'Key': "text_test_string.txt"}, ExpiresIn=300)

print(response)