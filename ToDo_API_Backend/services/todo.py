from fastapi.responses import JSONResponse
from models.todo import Task as TaskModel
from schemas.todo import Task
import secrets

class TaskService():
    
    def __init__(self, db) -> None:
        self.db = db
    
    def get_tasks(self):
        tasks_ref = self.db.collection("tasks").stream()
        query =  [{"id": doc.id, **doc.to_dict()} for doc in tasks_ref]       
        return query
    
    def get_task(self, task_id):
        doc = self.db.collection("tasks").document(task_id).get()    
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        
        return {"id": doc.id, **doc.to_dict()}
    
    def get_task_by_priority(self, priority):
        query = self.db.query(TaskModel).filter(TaskModel.priority == priority).all()      
        return query
    
    def create_task(self, task:Task):
        task_id = secrets.token_hex(10)
        self.db.collection("tasks").document(task_id).set(task.dict())
        return {"id": task_id, **task.dict()}
    
    def update_task(self, task_id: str, task:Task):
        doc_ref = self.db.collection("tasks").document(task_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="Tarea no encontrada")
        doc_ref.update(task.dict())
        return {"id": task_id, **task.dict()}
    
    def delete_task(self, task_id:str):        
        doc_ref = self.db.collection("tasks").document(task_id)
        if not doc_ref.get().exists:
            return {"message": "NO se encontro registro", "status": 404}
        else:
            doc_ref.delete()
            return {"message": "Tarea eliminada", "status": 201}
