from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_current_user
from app.db.session import get_db
from app.schemas.pool import (
    PoolCreate, PoolUpdate, PoolResponse,
    PoolOrderCreate, PoolOrderResponse
)
from app.db.repositories.pool import PoolRepository, PoolOrderRepository
from app.db.models.user import User
from app.websockets.connection import ConnectionManager

router = APIRouter()

@router.post("/", response_model=PoolResponse)
async def create_pool(
    pool: PoolCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = PoolRepository(db)
    return repo.create(pool)

@router.get("/active", response_model=List[PoolResponse])
async def get_active_pools(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = PoolRepository(db)
    return repo.get_active_pools()

@router.post("/{pool_id}/orders", response_model=PoolOrderResponse)
async def add_order_to_pool(
    pool_id: int,
    order: PoolOrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pool_repo = PoolRepository(db)
    pool = pool_repo.get_by_id(pool_id)
    if not pool or not pool.status:
        raise HTTPException(status_code=404, detail="Active pool not found")

    order_repo = PoolOrderRepository(db)
    new_order = order_repo.create(pool_id, current_user.id, order)
    # await ConnectionManager.broadcast_to_pool(
    #     pool_id,
    #     {
    #         "type": "new_order",
    #         "data": {
    #             "id": new_order.id,
    #             "pool_id": new_order.pool_id,
    #             "user_id": new_order.user_id,
    #             "food_id": new_order.food_id,
    #             "quantity": new_order.quantity,
    #             "user_full_name": new_order.user.full_name,
    #             "food_name": new_order.food.name
    #         }
    #     }
    # )
    print(12313)
    return new_order

@router.put("/{pool_id}/close")
async def close_pool(
    pool_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = PoolRepository(db)
    pool = repo.close_pool(pool_id)
    if not pool:
        raise HTTPException(status_code=404, detail="Pool not found")
    return {"message": "Pool closed successfully"}