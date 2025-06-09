from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://super_user:123456@localhost/concert_api"

engine = create_engine(DATABASE_URL, echo=True)

Session_Local = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind= engine
)

Base = declarative_base()

def get_db() -> Session:

    db = Session_Local()
    try:
        yield db  # give db session to the endpoint
    finally:
        db.close()  # clean up after request