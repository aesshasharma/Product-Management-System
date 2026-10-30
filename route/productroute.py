from fastapi import APIRouter, HTTPException
from model.productmodel import Product
from controller import productcontroller

router = APIRouter()

@router.post("/products")
def create_product(product: Product):
    result = productcontroller.create_product(product)
    if result is None:
        raise HTTPException(status_code=400, detail="ID already exists")
    return result

@router.get("/products")
def get_all_products():
    return productcontroller.get_all_products()

@router.get("/products/{product_id}")
def get_product(product_id: int):
    result = productcontroller.get_product(product_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@router.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    result = productcontroller.update_product(product_id, product)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    result = productcontroller.delete_product(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}