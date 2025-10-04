from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    images: List[str]
    location: str
    address: str
    dateRange: str
    price: float
    rating: float
    currency: str
    discount: float | None = None