from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Subscriber(Base):
    __tablename__ = "subscribers"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    project = Column(String, nullable=False)
    location = Column(String, nullable=True)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    subscribe_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    subscribe_date = Column(Date, default=datetime)