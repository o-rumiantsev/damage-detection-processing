from shapely.wkb import loads

from src.core import polygons_storage


async def get_many():
    polygons = await polygons_storage.get_many()
    return [to_dto(polygon) for polygon in polygons]


def to_dto(polygon):
    wkt_element = polygon.polygon
    shapely_polygon = loads(bytes(wkt_element.data))
    coordinates = list(shapely_polygon.exterior.coords)
    return {"damage_class": polygon.damage_class, "coordinates": coordinates}
