from typing import List

from fastapi import APIRouter, HTTPException, status

from models import User, Product
from data import mockUsers as users, mockProducts as products

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users():
    return users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next(
        (
            user 
            for user 
            in users 
            if user["id"] == user_id
        ),
        None
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User does not exist"
        )
    
    return user

@router.get("/{user_id}/favorite", response_model=List[Product])
def get_user_favorite(user_id: int):
    user = next(
        (
            user 
            for user 
            in users 
            if user["id"] == user_id
        ),
        None
    )

    favorite_products = [
        Product(**product) 
        for product 
        in products 
        if product["id"] in user["favorites"]
    ]

    return favorite_products
