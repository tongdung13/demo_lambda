from fastapi import APIRouter




router = APIRouter()


async def hello():
    return {"hello": "world"}