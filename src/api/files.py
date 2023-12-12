import asyncio
import uuid

from fastapi import File, UploadFile

from src import logger
from src.core import files_storage


async def create_many(files: list[UploadFile]):
    tasks = []

    logger.info(f'Saving {len(files)} files')

    for file in files:
        tasks.append(create(file))

    created_files = await asyncio.gather(*tasks)

    logger.info(f'Successfully saved {len(files)} files')

    return created_files


async def create(file: File):
    file_id = str(uuid.uuid4())

    await files_storage.save(file_id, file)

    logger.info(f'Successfully saved file "{file.filename}" as "{file_id}"')

    return {"file_name": file.filename, "file_id": file_id}
