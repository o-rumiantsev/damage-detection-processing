import tensorflow as tf
from aiofiles.tempfile import TemporaryFile
from rasterio import MemoryFile

from src import files_storage


async def save(file_id: str, file: TemporaryFile):
    await files_storage.upload(file_id, file.file)


async def get(file_id):
    buffer = await files_storage.download(file_id)
    image, metadata = read_tiff_image(buffer)
    image = image.transpose(1, 2, 0)
    image = reshape_image(image)
    return image, metadata


def read_tiff_image(buffer):
    with MemoryFile(buffer) as file:
        with file.open() as dataset:
            return dataset.read(), (dataset.crs, dataset.transform)


def reshape_image(image):
    crop_size = max(image.shape[0], image.shape[1])

    cropped_image = tf.image.resize_with_crop_or_pad(image, crop_size, crop_size)
    cropped_image = cropped_image[:, :, :3]

    resized_image = tf.image.resize(cropped_image, [1024, 1024])

    return resized_image
