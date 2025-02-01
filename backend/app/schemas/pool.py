from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class PoolOrderBase(BaseModel):
    food_id: int
    quantity: int = 1

class PoolOrderCreate(PoolOrderBase):
    pass

class PoolOrderResponse(PoolOrderBase):
    id: int
    pool_id: int
    user_id: int
    created_at: datetime
    user_full_name: str
    food_name: str

    class Config:
        from_attributes = True

class PoolBase(BaseModel):
    name: str

class PoolCreate(PoolBase):
    pass

class PoolUpdate(BaseModel):
    status: Optional[bool] = None

class PoolResponse(PoolBase):
    id: int
    status: bool
    created_at: datetime
    closed_at: Optional[datetime]
    orders: List[PoolOrderResponse]

    class Config:
        from_attributes = True