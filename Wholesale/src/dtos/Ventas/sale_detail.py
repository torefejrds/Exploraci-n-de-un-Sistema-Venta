# models/sale_detail.py
from pydantic import BaseModel

class SaleDetail(BaseModel):
    id: int
    sale_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float
