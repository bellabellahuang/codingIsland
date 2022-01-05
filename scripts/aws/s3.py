import boto3
import os


class S3Service:
    def __init__(self):
        self.service = boto3.client('s3', region_name="us-west-2")
        self.bucket = os.environ.get('TEST_BUCKET')

    def get_file_size(self, key: str, bucket: str = None) -> int:
        bucket = self.bucket if bucket is None else bucket
        response = self.list_object(bucket, key)
        if not response: return 0
        for obj in response.get('Contents', []):
            if obj['Key'] == key:
                return obj['Size']
        return 0

    def upload(self, file: str, location: str) -> bool:
        self.service.upload_file(file, self.bucket, location)
        return True

    def get_object(self, bucket: str, key: str):
        try:
            return self.service.get_object(Bucket=bucket, Key=key)
        except Exception:
            return False

    def head_object(self, bucket: str, key: str):
        try:
            self.service.head_object(Bucket=bucket, Key=key)
            return True
        except Exception:
            return False

    def list_object(self, bucket: str, prefix: str):
        try:
            return self.service.list_objects_v2(Bucket=bucket, Prefix=prefix)
        except Exception:
            return False

    def download(self, bucket: str, key: str, file: str):
        self.service.download_file(bucket, key, file)
