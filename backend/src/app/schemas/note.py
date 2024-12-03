# schemas/note.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    content: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    temperature: float
    updated_date: Optional[datetime] = None  # Make this field optional



class Note(NoteBase):
    id: int
    session_id: int
    creation_date: datetime
    updated_date: datetime

    model_config = {'from attributes': True}


