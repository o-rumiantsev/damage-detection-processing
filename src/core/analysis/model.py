import tensorflow as tf


def load_model(filepath):
    return tf.keras.models.load_model(filepath, compile=False)


def predict(model, image):
    test_data = tf.data.Dataset.from_tensor_slices([image]).batch(1)

    image_as_batch = next(iter(test_data.take(1)))
    predictions = model.predict(image_as_batch)
    predicted_mask = tf.constant(predictions[0])

    return tf.where(predicted_mask > 0.5, 1.0, 0.0)
