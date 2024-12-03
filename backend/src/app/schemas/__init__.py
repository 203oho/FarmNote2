"""
The schema package contains the api models.
They are used as DTOs (Data-Transfer-Objects) and to validate the given input
"""
from .note import Note
from .note import NoteBase
from .session import Session
from .token import get_a_session_token

