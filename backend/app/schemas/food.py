from pydantic import BaseModel, Field
from typing import Optional

class FoodBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class FoodCreate(FoodBase):
    pass

class FoodUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

class FoodResponse(FoodBase):
    id: int

    class Config:
        from_attributes = True