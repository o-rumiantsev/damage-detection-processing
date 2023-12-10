import numpy as np
from skimage.measure import find_contours, approximate_polygon

DAMAGE_CLASSES = [
    'background',
    'no-damage',
    'minor-damage',
    'major-damage',
    'destroyed',
    'unclassified',
]

MIN_AREA_THRESHOLD = 1000


def shoelace_area(vertices):
    x = vertices[:, 0]
    y = vertices[:, 1]
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def get_polygons(mask):
    polygons = {
        'background': [],
        'no-damage': [],
        'minor-damage': [],
        'major-damage': [],
        'destroyed': [],
        'unclassified': [],
    }

    for class_index in range(mask.shape[2]):
        if class_index == 0 or class_index == 5:
            continue

        damage_class = DAMAGE_CLASSES[class_index]
        binary_mask = mask[:, :, class_index].numpy().astype(bool)

        contours = find_contours(binary_mask)

        for contour in contours:
            polygon = approximate_polygon(contour, tolerance=3)
            polygon_area = shoelace_area(polygon)
            if polygon_area > MIN_AREA_THRESHOLD:
                polygons[damage_class].append(polygon)

    return polygons
