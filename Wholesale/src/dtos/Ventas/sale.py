# models/sale.py
from pydantic import BaseModel
from datetime import datetime

class Sale(BaseModel):
    id: int
    folio: str
    location_id: int
    datetime: datetime
    total: float
    status: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
