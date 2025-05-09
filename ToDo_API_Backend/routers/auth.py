from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from schemas.user import User


auth_router = APIRouter()

@auth_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "123456789":
        token: str = create_token(user.model_dump())
        return JSONResponse(content=token, status_code=200)