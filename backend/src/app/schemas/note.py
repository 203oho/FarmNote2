# schemas/note.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    content: str
    latitude: float
    longitude: float
    temperature: float



class Note(NoteBase):
    id: int
    session_id: int
    creation_date: datetime
    updated_date: datetime

    model_config = {'from attributes': True}
