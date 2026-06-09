# dtos/sale_dto.py
from pydantic import BaseModel
from typing import List
from dtos.sale_detail_dto import SaleDetailDTO

class SaleDTO(BaseModel):
    location_id: int
    status: str
    details: List[SaleDetailDTO]
    


