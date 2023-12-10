from src.config import MODEL
from src.core.analysis.geometry import get_polygons
from src.core.analysis.model import load_model, predict

model = load_model(MODEL)


def process_image(image):
    mask = predict(model, image)
    polygons = get_polygons(mask)
    return polygons, mask
