
from pydantic import BaseModel

class Store_Items(BaseModel):
    id: int
    name: str
    description: str
    price: float

