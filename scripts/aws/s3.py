import boto3
import os
import gzip
from io import BytesIO


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

    def get_object_content(self, bucket: str, key: str) -> str:
        return self.get_object(bucket, key)['Body'].read().decode('utf-8')

    def get_gzip_file_content(self, bucket: str, key: str) -> str:
        response = self.get_object(bucket, key)['Body'].read() # bytes
        return gzip.GzipFile(fileobj=BytesIO(response)).read().decode('utf-8')

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

    def save_file(self, file_name: str, content: str):
        self.service.put_object(
            Bucket=self.bucket,
            Key=file_name,
            Body=self.gzip_content(content))

    def gzip_content(self, content):
        file_obj = BytesIO()
        if isinstance(content, str):
            content = content.encode('utf-8')
        gzip.GzipFile(fileobj=file_obj, mode='wb').write(content)
        return file_obj.getvalue()
