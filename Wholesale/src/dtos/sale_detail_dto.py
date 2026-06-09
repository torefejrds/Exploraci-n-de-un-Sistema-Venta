# dtos/sale_detail_dto.py
from pydantic import BaseModel

class SaleDetailDTO(BaseModel):
    product_id: int
    quantity: int
