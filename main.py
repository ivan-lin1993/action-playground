import os
import requests
import boto3


s3 = boto3.client("s3")

file = open("test", 'w')
file.write(f"{os.environ.get('mysecret')}")
file.close()

with open("test", "rb") as f:
    s3.upload_fileobj(f, "mxdr-dev-ivan-cft-templates-bucket", "testfile")