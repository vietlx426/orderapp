from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_current_user
from app.db.session import get_db
from app.schemas.food import FoodCreate, FoodUpdate, FoodResponse
from app.db.repositories.food import FoodRepository
from app.db.models.user import User

router = APIRouter()

@router.post("/", response_model=FoodResponse)
async def create_food(
    food: FoodCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = FoodRepository(db)
    return repo.create(food)

@router.get("/", response_model=List[FoodResponse])
async def get_foods(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = FoodRepository(db)
    return repo.get_all(skip=skip, limit=limit)

@router.get("/{food_id}", response_model=FoodResponse)
async def get_food(
    food_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = FoodRepository(db)
    food = repo.get_by_id(food_id)
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@router.put("/{food_id}", response_model=FoodResponse)
async def update_food(
    food_id: int,
    food_data: FoodUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = FoodRepository(db)
    food = repo.update(food_id, food_data)
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@router.delete("/{food_id}")
async def delete_food(
    food_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    repo = FoodRepository(db)
    if not repo.delete(food_id):
        raise HTTPException(status_code=404, detail="Food not found")
    return {"message": "Food deleted"}