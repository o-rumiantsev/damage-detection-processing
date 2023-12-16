from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Polygon(Base):
    __tablename__ = 'polygons'
    id = Column(Integer, primary_key=True)
    damage_class = Column(String)
    polygon = Column(Geometry('POLYGON', srid=4326))
    created_at = Column(DateTime, default=datetime.utcnow)
