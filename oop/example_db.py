from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.engine import create_engine
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime,default=datetime.now)

class PythonNews(Base):
    __tablename__ = 'python_news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    summary = Column(String)
    link = Column(String)
    added_on = Column(DateTime, default=datetime.now)

if __name__ == "__main__":
    engine =  create_engine('sqlite:///demo.sqlite3', echo=True)
    Base.metadata.create_all(engine)
    