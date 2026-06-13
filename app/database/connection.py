from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autoflush= False, autocommit = False, bind= engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()