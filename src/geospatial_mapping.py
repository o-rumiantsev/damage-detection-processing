import rasterio
from rasterio import warp

TARGET_CRS = 'EPSG:4326'


def get_geospatial_metadata(file_path):
    with rasterio.open(file_path) as dataset:
        return dataset.crs, dataset.transform


def polygons_to_geospatial(polygons, metadata):
    crs, transform = metadata
    geospatial_polygons = []

    for polygon in polygons:
        geospatial_polygon = [rasterio.transform.xy(transform, point[0], point[1]) for point in polygon]
        x_coords, y_coords = zip(*geospatial_polygon)
        transformed_x_coords, transformed_y_coords = warp.transform(crs, TARGET_CRS, x_coords, y_coords)
        geospatial_polygon = list(zip(transformed_x_coords, transformed_y_coords))
        geospatial_polygons.append(geospatial_polygon)

    return geospatial_polygons
