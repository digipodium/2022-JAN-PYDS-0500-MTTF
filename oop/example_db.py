from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.engine import create_engine
from datetime import datetime

Base = declarative_base()

class Pet(Base):
    
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    age = Column(Integer)
    pettype = Column(String(15))
    owner = Column(String(25))
    added_at = Column(DateTime, default=datetime.now())

if __name__ == "__main__":
    engine =  create_engine('sqlite:///pets.sqlite3', echo=True)
    Base.metadata.create_all(engine)
    