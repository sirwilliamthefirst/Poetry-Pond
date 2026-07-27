from fastapi import APIRouter

from app.routes import user
from app.routes import poem

api_router = APIRouter(
    prefix="/api",
)

api_router.include_router(user.router)
api_router.include_router(poem.router)

