from botocore.exceptions import NoCredentialsError

from src import logger
from src.config import AWS_S3_BUCKET
from src.files_storage.client import create_client


async def download(file_id):
    async with create_client() as client:
        try:
            response = await client.get_object(Bucket=AWS_S3_BUCKET, Key=file_id)
            return await response['Body'].read()
        except NoCredentialsError:
            logger.error("Credentials not available")
        except Exception as exception:
            logger.error(f'Failed to download file {file_id}', exception)
