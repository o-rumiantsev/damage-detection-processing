import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
QUEUE_URL = os.environ.get('QUEUE_URL')

MODEL = 'models/fine-tune-2023-12-18T09_54_17.h5'

SRID = 4326

COORDINATE_REFERENCE_SYSTEM = f'EPSG:{SRID}'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_BUCKET = 'damage-detection-satellite-images'
