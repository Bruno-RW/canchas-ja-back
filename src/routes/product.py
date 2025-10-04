from typing import List

from fastapi import APIRouter, HTTPException, status

from models import Product
from data import mockUsers as users, mockProducts as products

router = APIRouter()

# ? === === === STATIC ROUTES === === === ?#
@router.get("/", response_model=List[Product])
def get_products():
    return [
        Product(**product)
        for product 
        in products
    ]

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
            status_code=status.HTTP_404_NOT_FOUND,
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No best-rated products found"
        )

    return best_rated_products


# ? === === === DYNAMIC ROUTES === === === ?#
@router.get("/near_you/{user_id}", response_model=List[Product])
def get_near_you(user_id: int):

    print(user_id)

    user = next(
        (
            user 
            for user 
            in users 
            if user["id"] == user_id
        ),
        None
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID '{user_id}' not found."
        )

    user_location = user["location"]

    near_you_products = [
        Product(**product) 
        for product 
        in products 
        if user_location in product["location"]
    ]

    if not near_you_products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products near you"
        )
    
    return near_you_products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next(
        (
            Product(**product)
            for product
            in products 
            if product["id"] == product_id
        ), 
        None
    )

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No product found"
        )
    
    return product
