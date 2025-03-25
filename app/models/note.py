from pydantic import BaseModel

class Note(BaseModel):
    id: str
    title: str
    description: str