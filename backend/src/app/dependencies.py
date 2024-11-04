

from fastapi import Header, HTTPException
from typing import Optional
import uuid

def get_session_token(session_token: Optional[str] = Header(None)) -> str:
    if session_token is None:
        # Generate a new session token if not provided
        session_token = str(uuid.uuid4())
    return session_token


