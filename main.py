from src.geospatial_mapping import get_geospatial_metadata, polygons_to_geospatial
from src.processing.process_image import process_image
from src.storage import store_polygons
from src.data_loader import load_image

image = load_image('test-data/mariupol-dram-theatre.tiff')
geospatial_metadata = get_geospatial_metadata('test-data/mariupol-dram-theatre.tiff')

polygons_by_class, _ = process_image(image)

geospatial_polygons_by_class = {}

for damage_class, class_polygons in polygons_by_class.items():
    geospatial_polygons_by_class[damage_class] = polygons_to_geospatial(class_polygons, geospatial_metadata)

store_polygons(geospatial_polygons_by_class)
