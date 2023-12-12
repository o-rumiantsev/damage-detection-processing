from src import logger
from src.core import files_storage, geospatial_mapping, polygons_storage
from src.core.analysis.process_image import process_image


async def analyze_file(file_id):
    image = files_storage.get(file_id)
    geospatial_metadata = geospatial_mapping.get_metadata(file_id)

    logger.info(f'Start processing file "{file_id}"')

    polygons_by_class, _ = process_image(image)

    logger.info(f'Finished processing file "{file_id}"')

    polygons = []

    for damage_class, class_polygons in polygons_by_class.items():
        geospatial_polygons = geospatial_mapping.to_geospatial(class_polygons,
                                                               geospatial_metadata)
        for polygon in geospatial_polygons:
            polygons.append({"damage_class": damage_class, "polygon": polygon})

    logger.info(f'Finished geospatial mapping for file "{file_id}"')

    await polygons_storage.save_many(polygons)
