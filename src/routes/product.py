from typing import List

from fastapi import APIRouter, HTTPException, status

from models import Product
from data import mockUsers as users, mockProducts as products

router = APIRouter()

@router.get("/", response_model=List[Product])
def get_products():
    return [
        Product(**product)
        for product 
        in products
    ]

# @router.get("/{product_id}", response_model=Product)
# def get_product(product_id: str):
#     product = next(
#         (
#             Product(**product)
#             for product
#             in products 
#             if product["id"] == product_id
#         ), 
#         None
#     )

#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="No product found"
#         )
    
#     return product

@router.get("/special_discount", response_model=List[Product])
def get_special_discount():
    discount_products = [
        Product(**product)
        for product
        in products
        if product.get("discount", 0) >= 50
    ]

    if not discount_products:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No product with discount equal or above 50%"
        )
    
    return discount_products

@router.get("/best_rated", response_model=List[Product])
def get_best_rated():
    best_rated_products = [
        Product(**product)
        for product
        in sorted(products, key=lambda x: x.get("rating", 0), reverse=True)[:5]
    ]

    if not best_rated_products:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No best-rated products found"
        )

    return best_rated_products

@router.get("/near_you", response_model=List[Product])
def get_near_you():
    current_user = users[0]
    user_location = current_user["location"]

    near_you_products = [
        Product(**product) 
        for product 
        in products 
        if user_location in product["location"]
    ]

    if not near_you_products:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No products near you"
        )
    
    return near_you_products
