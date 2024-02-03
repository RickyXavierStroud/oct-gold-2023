import boto3

s3 = boto3.client('s3')

s3.upload_file('text_test.txt', 'rxs-101623', 'text_test_upload.txt', ExtraArgs={'ContentType':'text/plain'})
