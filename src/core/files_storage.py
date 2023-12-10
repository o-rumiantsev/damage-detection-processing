import os

import aiofiles
import rasterio
import tensorflow as tf
from aiofiles.tempfile import TemporaryFile

from src.config import FILE_STORAGE_PATH, FILE_READ_SIZE


def get(file_id):
    path = os.path.join(FILE_STORAGE_PATH, file_id)
    image = read_tiff_image(path)
    image = image.transpose(1, 2, 0)
    return reshape_image(image)


def read_tiff_image(file_path):
    with rasterio.open(file_path) as dataset:
        return dataset.read()


def reshape_image(image):
    crop_size = max(image.shape[0], image.shape[1])

    cropped_image = tf.image.resize_with_crop_or_pad(image, crop_size, crop_size)
    cropped_image = cropped_image[:, :, :3]

    resized_image = tf.image.resize(cropped_image, [1024, 1024])

    return resized_image


async def save(file_id: str, file: TemporaryFile):
    file_path = os.path.join(FILE_STORAGE_PATH, file_id)

    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(FILE_READ_SIZE):
            await out_file.write(content)
