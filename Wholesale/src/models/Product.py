# models/product.py
from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id: int
    barcode: str
    name: str
    description: str
    brand: str
    price: float
    stock: int
    active: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


# models/product.py
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
