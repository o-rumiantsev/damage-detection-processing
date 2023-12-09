import rasterio
import tensorflow as tf


def load_image(path):
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
