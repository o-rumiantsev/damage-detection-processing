from src.processing.geometry import get_polygons
from src.processing.model import load_model, predict

MODEL = 'models/damage-detector-2023-12-04T13_41_55.h5'

model = load_model(MODEL)


def process_image(image):
    mask = predict(model, image)
    polygons = get_polygons(mask)
    return polygons, mask
