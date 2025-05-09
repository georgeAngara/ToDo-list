from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routers.todo import todo_router
from routers.auth import auth_router
from routers.home import home_router
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()
app.title = "ToDo API"
app.version = '0.0.1'


# origins = [
#     "http://localhost:5173",   # Vite dev
#     "http://localhost:8080",   # Vite preview o servidor local
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puerto de Vite por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)

app.include_router(home_router)
app.include_router(auth_router)
app.include_router(todo_router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)