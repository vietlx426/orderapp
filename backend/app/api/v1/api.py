from fastapi import APIRouter
from app.api.v1.endpoints import user, auth, food, pool

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(food.router, prefix="/food", tags=["food"])
api_router.include_router(pool.router, prefix="/pool", tags=["pool"])

