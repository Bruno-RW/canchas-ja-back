from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    images: List[str]

    details: str
    description: str

    location: str
    address: str

    dateRange: str
    price: float

    currency: str
    discountPercentage: float | None = None
    discountDuration: float | None = None

    rating: float
    reviews: int