import asyncio
import uuid

from fastapi import File, UploadFile

from src.core import files_storage


async def create_many(files: list[UploadFile]):
    tasks = []

    for file in files:
        tasks.append(create(file))

    created_files = await asyncio.gather(*tasks)

    return created_files


async def create(file: File):
    file_id = str(uuid.uuid4())

    await files_storage.save(file_id, file)

    return {"file_name": file.filename, "file_id": file_id}
