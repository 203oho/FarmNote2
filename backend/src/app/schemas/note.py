
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: str
    location: Optional[str] = None
    category: Optional[str] = None

class NoteCreate(NoteBase):
    pass  # You can add any additional fields if needed

class Note(NoteBase):
    id: int
    created_at: datetime




