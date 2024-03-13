from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from .config import settings

url = URL.create('postgresql', username=settings.database_username, password=settings.database_password, host=settings.database_hostname,port=settings.database_port, database=settings.database_name)

engine = create_engine(url='postgres://fastapi_6d8i_user:x9ndmCBKhMA1kEFwrohCvfM2qYaeeSUb@dpg-cnopajvjbltc73fk4kt0-a.oregon-postgres.render.com/fastapi_6d8i')

SessionLocal = sessionmaker(autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()