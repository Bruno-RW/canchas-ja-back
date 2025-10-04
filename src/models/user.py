from typing import List, Literal
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    type: Literal["C", "H"]  # C = Client | H = Host
    avatar: str
    initials: str
    location: str
    favorites: List[int] | None = None