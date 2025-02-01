from sqlalchemy.orm import Session
from app.db.models.food import Food
from app.schemas.food import FoodCreate, FoodUpdate

class FoodRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, food: FoodCreate) -> Food:
        db_food = Food(**food.model_dump())
        self.db.add(db_food)
        self.db.commit()
        self.db.refresh(db_food)
        return db_food

    def get_by_id(self, food_id: int) -> Food:
        return self.db.query(Food).filter(Food.id == food_id).first()

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Food).offset(skip).limit(limit).all()

    def update(self, food_id: int, food_data: FoodUpdate) -> Food:
        db_food = self.get_by_id(food_id)
        if db_food:
            update_data = food_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_food, field, value)
            self.db.commit()
            self.db.refresh(db_food)
        return db_food

    def delete(self, food_id: int) -> bool:
        db_food = self.get_by_id(food_id)
        if db_food:
            self.db.delete(db_food)
            self.db.commit()
            return True
        return False