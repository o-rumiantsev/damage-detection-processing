from src.core import files_storage, polygons_storage, geospatial_mapping
from src.core.analysis.process_image import process_image


async def create(file_id):
    image = files_storage.get(file_id)
    geospatial_metadata = geospatial_mapping.get_metadata(file_id)

    polygons_by_class, _ = process_image(image)

    polygons = []

    for damage_class, class_polygons in polygons_by_class.items():
        geospatial_polygons = geospatial_mapping.to_geospatial(class_polygons,
                                                               geospatial_metadata)
        for polygon in geospatial_polygons:
            polygons.append({"damage_class": damage_class, "polygon": polygon})

    await polygons_storage.save_many(polygons)
