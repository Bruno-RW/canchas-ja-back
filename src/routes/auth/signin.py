from fastapi import APIRouter
from pydantic import BaseModel

from data import mockUsers as users, mockProducts as products

router = APIRouter()

class SigninRequest(BaseModel):
    name: str
    email: str
    password: str
    confirmPassword: str
    location: str = ""

@router.post("/signin", response_model=dict)
def signin_user(request: SigninRequest):
    if any(user["email"] == request.email for user in users):
        return {"error": "Email already exists"}
    
    if request.password != request.confirmPassword:
        return {"error": "Passwords do not match"}

    name = request.name.strip() if request.name else ""
    initials = "".join([word[0] for word in name.split()]) if name else ""

    new_user = {
        "id": len(users) + 1,
        "name": request.name,
        "email": request.email,
        "type": "C",  # Default to Client
        "avatar": "/placeholder.svg?height=40&width=40",
        "initials": initials,
        "isLogin": False,
        "location": request.location,
        "favorites": [],
        "password": request.password,
    }

    users.append(new_user)
    return {"message": "User created successfully", "user": new_user}