from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

create_session = sessionmaker(bind=engine)
