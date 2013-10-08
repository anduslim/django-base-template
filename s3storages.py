from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


# Define bucket and folder for static files.
StaticStorage = lambda: S3BotoStorage(
    bucket=settings.S3_BUCKET_NAME,
    location='assets')

# Define bucket and folder for media files.
MediaStorage  = lambda: S3BotoStorage(
    bucket=settings.S3_BUCKET_NAME,
    location='media')

