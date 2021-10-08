import boto3
from ..config import CONFIG


class Util:
    def s3upload(file, filename):

        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id=CONFIG.AccessKeyId,
                aws_secret_access_key=CONFIG.SecretKey,
            )

            region = CONFIG.region

            bucket_name = CONFIG.bucket_name
            s3.upload_fileobj(
                file, bucket_name, filename, ExtraArgs={"ACL": "public-read"}
            )

            url = "https://s3-%s.amazonaws.com/%s/%s" % (region, bucket_name, filename)

        except Exception as e:
            return e

        return url

    def s3delete(filename):

        s3 = boto3.client(
            "s3",
            aws_access_key_id=CONFIG.AccessKeyId,
            aws_secret_access_key=CONFIG.SecretKey,
        )

        bucket_name = CONFIG.bucket_name
        s3.delete_object(Bucket=bucket_name, Key=filename)
