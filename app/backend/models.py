from pydantic import BaseModel

class Task(BaseModel):
    title: str
    due_date: str
    description: str
