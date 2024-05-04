from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Sessiom = sessionmaker(bind=engine)
session = Sessiom()

Base = declarative_base()
Base.metadata.create_all(engine)