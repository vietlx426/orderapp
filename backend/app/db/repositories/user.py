from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreate) -> User:
        db_user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            is_shipper=user_data.is_shipper,
            hashed_password=get_password_hash(user_data.password)
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(
            User.id == user_id,
            User.deleted_at.is_(None)
        ).first()

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(
            User.email == email,
            User.deleted_at.is_(None)
        ).first()

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).filter(
            User.deleted_at.is_(None)
        ).offset(skip).limit(limit).all()

    def update(self, user_id: int, user_data: UserUpdate) -> User:
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        update_data = user_data.model_dump(exclude_unset=True)
        
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(db_user, field, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def soft_delete(self, user_id: int) -> bool:
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False

        db_user.deleted_at = datetime.utcnow()
        db_user.is_active = False
        self.db.commit()
        return True