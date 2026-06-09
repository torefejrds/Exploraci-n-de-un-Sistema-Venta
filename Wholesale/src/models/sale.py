# models/sale.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from config.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    folio = Column(String, unique=True, index=True)
    location_id = Column(Integer)
    datetime = Column(DateTime, default=datetime.now)
    total = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
