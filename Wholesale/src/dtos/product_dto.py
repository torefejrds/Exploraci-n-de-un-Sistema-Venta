# dtos/product_dto.py
from pydantic import BaseModel

class ProductDTO(BaseModel):
    name: str
    description: str
    brand: str
    price: float
    stock: int
