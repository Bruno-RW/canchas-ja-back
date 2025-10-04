from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import (
    login,
    signin,

    user,
    product
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router, prefix="/api/v1", tags=["Auth"])
app.include_router(signin.router, prefix="/api/v1", tags=["Auth"])

app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(product.router, prefix="/api/v1/product", tags=["Product"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}