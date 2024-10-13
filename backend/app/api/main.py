from fastapi import APIRouter
from app.api.routes import hello_world

api_router = APIRouter()

print("Including hello_world routes")
api_router.include_router(hello_world.router, tags=["Items"])