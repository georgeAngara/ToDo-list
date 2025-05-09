from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()

@home_router.get('/', tags=['Home'])
def menssage():
    return HTMLResponse('<h1>Gestionar una lista de "tareas" (to-do)</h1>')