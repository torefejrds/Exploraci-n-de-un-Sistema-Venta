# routes/sale_routes.py
from fastapi import APIRouter
from dtos.Ventas.sale import Sale
from models.sale_detail import SaleDetail
from dtos.sale_dto import SaleDTO
from datetime import datetime

router = APIRouter(prefix="/sales", tags=["Sales"])

sales = []

@router.get("/")
def list_sales():
    return sales

@router.post("/")
def create_sale(dto: SaleDTO):
    folio = f"FOLIO{len(sales)+1:05}"
    total = 0
    details = []
    for d in dto.details:
        unit_price = 100.0  # precio de prueba
        subtotal = d.quantity * unit_price
        total += subtotal
        details.append(SaleDetail(
            id=len(details)+1,
            sale_id=len(sales)+1,
            product_id=d.product_id,
            quantity=d.quantity,
            unit_price=unit_price,
            subtotal=subtotal
        ))
    new_sale = Sale(
        id=len(sales)+1,
        folio=folio,
        location_id=dto.location_id,
        datetime=datetime.now(),
        total=total,
        status=dto.status
    )
    sales.append({"sale": new_sale, "details": details})
    return new_sale
  
  # routes/sale_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from services import sale_service
from dtos.sale_dto import SaleDTO

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.post("/")
def create_sale(dto: SaleDTO, db: Session = Depends(get_db)):
    return sale_service.create_sale(db, dto)

@router.get("/")
def list_sales(db: Session = Depends(get_db)):
    return db.query(Sale).all()
