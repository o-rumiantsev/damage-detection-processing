MODEL = 'models/damage-detector-2023-12-04T13_41_55.h5'

FILE_READ_SIZE = 1024

FILE_STORAGE_PATH = 'file-storage'

SRID = 4326

COORDINATE_REFERENCE_SYSTEM = f'EPSG:{SRID}'

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:35432/damage-detection"
