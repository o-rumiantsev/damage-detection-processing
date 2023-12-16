from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon as ShapelyPolygon

from src import logger
from src.config import SRID
from src.database.models import Polygon
from src.database.sql import create_session


def save_many(polygons):
    with create_session() as session:
        logger.info(f'Saving {len(polygons)} polygons')
        for polygon in polygons:
            shapely_polygon = ShapelyPolygon(polygon['polygon'])
            session.add(Polygon(
                damage_class=polygon['damage_class'],
                polygon=from_shape(shapely_polygon, srid=SRID)
            ))

        session.commit()
        logger.info(f'Saved {len(polygons)} polygons')


def get_many():
    with create_session() as session:
        return session.query(Polygon).all()
