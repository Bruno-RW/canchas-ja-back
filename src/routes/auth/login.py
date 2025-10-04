from fastapi import APIRouter, HTTPException, status

from data import mockUsers as users
from models import LoginRequest, User

router = APIRouter()

@router.post("/login", response_model=User)
def login_user(request: LoginRequest):
    user = next(
        (
            user 
            for user 
            in users 
            if user["email"] == request.email\
                and user["password"] == request.password
        ),
        None
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return User(**user)