# routes/product_routes.py
from fastapi import APIRouter
from models import Product
from dtos.product_dto import ProductDTO

router = APIRouter(prefix="/products", tags=["Products"])

# Datos de prueba
products = []

@router.get("/")
def list_products():
    return products

@router.post("/")
def create_product(dto: ProductDTO):
    new_product = Product(
        id=len(products)+1,
        barcode=f"BC{len(products)+1:05}",
        name=dto.name,
        description=dto.description,
        brand=dto.brand,
        price=dto.price,
        stock=dto.stock,
        active=True
    )
    products.append(new_product)
    return new_product

@router.put("/{product_id}")
def update_product(product_id: int, dto: ProductDTO):
    for p in products:
        if p.id == product_id:
            p.name = dto.name
            p.description = dto.description
            p.brand = dto.brand
            p.price = dto.price
            p.stock = dto.stock
            return p
    return {"error": "Product not found"}

@router.delete("/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p.id == product_id:
            p.active = False
            return {"message": "Product deactivated"}
    return {"error": "Product not found"}
