from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.pool import Pool, PoolOrder
from app.schemas.pool import PoolCreate, PoolUpdate, PoolOrderCreate

class PoolRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, pool_data: PoolCreate) -> Pool:
        db_pool = Pool(**pool_data.model_dump())
        self.db.add(db_pool)
        self.db.commit()
        self.db.refresh(db_pool)
        return db_pool

    def get_active_pools(self):
        return self.db.query(Pool).filter(Pool.status == True).all()

    def get_by_id(self, pool_id: int) -> Pool:
        return self.db.query(Pool).filter(Pool.id == pool_id).first()

    def close_pool(self, pool_id: int) -> Pool:
        pool = self.get_by_id(pool_id)
        if pool:
            pool.status = False
            pool.closed_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(pool)
        return pool

class PoolOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, pool_id: int, user_id: int, order_data: PoolOrderCreate) -> PoolOrder:
        db_order = PoolOrder(
            pool_id=pool_id,
            user_id=user_id,
            **order_data.model_dump()
        )
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_pool_orders(self, pool_id: int):
        return self.db.query(PoolOrder).filter(PoolOrder.pool_id == pool_id).all()
    
    def get_pool_with_orders(self, pool_id: int):
        pool = self.db.query(Pool).filter(Pool.id == pool_id).first()
        if pool:
            orders = self.db.query(PoolOrder)\
                .filter(PoolOrder.pool_id == pool_id)\
                .all()
            return {
                "pool_id": pool_id,
                "orders": [{
                    "id": order.id,
                    "pool_id": order.pool_id,
                    "user_id": order.user_id,
                    "food_id": order.food_id,
                    "quantity": order.quantity,
                    "user_full_name": order.user.full_name,
                    "food_name": order.food.name,
                    "created_at": order.created_at
                } for order in orders]
            }
        return None