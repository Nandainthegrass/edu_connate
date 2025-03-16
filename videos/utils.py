import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.conf import settings


def upload_to_s3(file, bucket_name, file_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    try:
        s3_client.upload_fileobj(file, bucket_name, file_name)
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return s3_url  # Return the S3 URL of the uploaded file
    except (NoCredentialsError, PartialCredentialsError):
        raise ValueError("Invalid AWS credentials")
    except Exception as e:
        raise ValueError(f"Failed to upload to S3: {e}")
