from botocore.exceptions import NoCredentialsError

from src import logger
from src.config import AWS_S3_BUCKET
from src.files_storage.client import create_client


async def upload(file_id, file):
    async with create_client() as client:
        try:
            await client.put_object(Bucket=AWS_S3_BUCKET, Key=file_id, Body=file)
        except NoCredentialsError:
            logger.error("Credentials not available")
        except Exception as exception:
            logger.error(f'Failed to upload file {file_id}', exception)
