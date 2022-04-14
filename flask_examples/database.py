from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.engine import create_engine
from datetime import datetime

Base = declarative_base()

class WebTest(Base):
    __tablename__ = 'webtests'
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    category = Column(String)
    get_ip = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.url

if __name__ == "__main__":
    engine =  create_engine('sqlite:///app.sqlite3', echo=True)
    Base.metadata.create_all(engine)
    