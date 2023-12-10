from datetime import datetime

from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon as ShapelyPolygon
from sqlalchemy import Column, Integer, String, DateTime, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL, SRID

engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class Polygon(Base):
    __tablename__ = 'polygons'
    id = Column(Integer, primary_key=True)
    damage_class = Column(String)
    polygon = Column(Geometry('POLYGON', srid=4326))
    created_at = Column(DateTime, default=datetime.utcnow)


# Create a configured "AsyncSession" class
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def save_many(polygons):
    async with AsyncSessionLocal() as session:
        for polygon in polygons:
            shapely_polygon = ShapelyPolygon(polygon['polygon'])
            session.add(Polygon(
                damage_class=polygon['damage_class'],
                polygon=from_shape(shapely_polygon, srid=SRID)
            ))

        await session.commit()


async def get_many():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Polygon))
        return result.scalars().all()
