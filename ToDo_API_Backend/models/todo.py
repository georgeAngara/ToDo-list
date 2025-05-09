from pydantic import BaseModel, validator, ValidationError
from typing import Optional

class Task(BaseModel):

    
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False
