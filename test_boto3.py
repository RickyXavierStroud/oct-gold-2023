import boto3

session = boto3.session() #represents a single connection to AWS

s3 = boto3.client('s3') #client gives us more control with AWS so we will use over Resources.
s3 = session.client('s3')

s3 = boto3.resource('s3') # calls from session but provides python's way to deal with things
s3 = session.resource('s3'
