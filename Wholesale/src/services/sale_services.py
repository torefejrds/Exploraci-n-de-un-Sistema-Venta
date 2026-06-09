# services/sale_service.py
from sqlalchemy.orm import Session
from models.sale import Sale
from models.sale_detail import SaleDetail
from models.Product import Product
import uuid
from datetime import datetime

def create_sale(db: Session, dto):
    folio = str(uuid.uuid4())[:8]  # folio único
    total = 0
    details = []

    for d in dto.details:
        product = db.query(Product).filter(Product.id == d.product_id).first()
        if not product or product.stock < d.quantity:
            raise Exception(f"Stock insuficiente para producto {d.product_id}")
        
        product.stock -= d.quantity
        subtotal = d.quantity * product.price
        total += subtotal

        detail = SaleDetail(
            sale_id=None,  # se asigna después
            product_id=d.product_id,
            quantity=d.quantity,
            unit_price=product.price,
            subtotal=subtotal
        )
        details.append(detail)

    new_sale = Sale(
        folio=folio,
        location_id=dto.location_id,
        datetime=datetime.now(),
        total=total,
        status=dto.status
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    for detail in details:
        detail.sale_id = new_sale.id
        db.add(detail)
    db.commit()

    return {"sale": new_sale, "details": details}
