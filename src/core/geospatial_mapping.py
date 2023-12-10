import os.path

import rasterio
from rasterio import warp

from src.config import COORDINATE_REFERENCE_SYSTEM, FILE_STORAGE_PATH


def get_metadata(file_id):
    file_path = os.path.join(FILE_STORAGE_PATH, file_id)
    with rasterio.open(file_path) as dataset:
        return dataset.crs, dataset.transform


def to_geospatial(polygons, metadata):
    crs, transform = metadata
    geospatial_polygons = []

    for polygon in polygons:
        geospatial_polygon = [rasterio.transform.xy(transform, point[0], point[1]) for point in polygon]
        x_coords, y_coords = zip(*geospatial_polygon)
        transformed_x_coords, transformed_y_coords = warp.transform(crs, COORDINATE_REFERENCE_SYSTEM, x_coords,
                                                                    y_coords)
        geospatial_polygon = list(zip(transformed_x_coords, transformed_y_coords))
        geospatial_polygons.append(geospatial_polygon)

    return geospatial_polygons
