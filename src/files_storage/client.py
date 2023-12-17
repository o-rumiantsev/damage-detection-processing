from aiobotocore.session import get_session

from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def create_client():
    session = get_session()
    return session.create_client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
