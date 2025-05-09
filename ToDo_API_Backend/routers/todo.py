from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Path, Query, HTTPException, Depends
from typing import List
from models.todo import Task as TaskModel
from services.todo import TaskService
from config.firestore_client import db
from schemas.todo import Task


todo_router = APIRouter()
todo_services = TaskService(db)


@todo_router.get('/tasks', tags=['Tasks'], response_model=List[Task])
def get_tasks() -> List[Task]:
    list_tasks = todo_services.get_tasks() 
    if not list_tasks:
        return JSONResponse(status_code=404, content={'message': 'No hay películas'}) 
    return JSONResponse(content=jsonable_encoder(list_tasks), status_code=200)

@todo_router.get('/task/{id}',tags=['Tasks'], response_model=Task)
def get_task(id: str) -> Task:
    data = todo_services.get_task(id) 
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(content=jsonable_encoder(data))

@todo_router.get('/tasks/', tags=['Tasks'], response_model=List[Task])
def get_tasks_by_priority(priority: str = Query(min_length=4, max_length=30, pattern="^(Alto|Medio|Bajo)$")) -> List[Task]:
    data =  todo_services.get_task_by_priority(priority)
    if not data:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(content=jsonable_encoder(data))

@todo_router.post('/tasks', tags=['Tasks'], response_model=dict)
def create_task(task: Task) -> dict:
    data = todo_services.create_task(task)   

    return JSONResponse(content={"message": "Se ha creado la tarea", "data":data} , status_code=201)

@todo_router.put('/task/{id}', tags=['Tasks'], response_model=dict)
def update_task(id: str, task: Task) -> dict:
    
    update_task = todo_services.get_task(id) 
    if not update_task:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})    
    
    todo_services.update_task(id, task)

    return JSONResponse(content={"message": "Se ha actializado la palícula", "data": update_task}, status_code=200)

@todo_router.delete('/tasks/{id}', tags=['Tasks'], response_model=dict)
def delete_task(id: str) -> dict:
    data = todo_services.delete_task(id)
    if int(data['status']) >= 400:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    else:
        return JSONResponse(content={"message": "Se ha eliminado", "data":[]} , status_code=201)
