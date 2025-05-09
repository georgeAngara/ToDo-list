from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Task(BaseModel):
    title: str = Field(max_length=20, min_length=4)
    description: str = Field(max_length=50, min_length=4)
    priority: str = Field(max_length=10, min_length=4)
    completed: bool = Field()    
    
    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    "title": "Task1",
                    "description": "Descripción de la tarea",
                    "priority": "Media",
                    "completed": True                
                }
            ]
    })  