import boto3
import os
from botocore.client import Config
from django.conf import settings


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

BUCKET_NAME = getattr(settings, "BUCKET_NAME", None)
REGION_NAME = getattr(settings, 'REGION_NAME', None)

# Get the S3 client and set it to Sig4 protocol
s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name=REGION_NAME,
                  config=Config(signature_version='s3v4'))