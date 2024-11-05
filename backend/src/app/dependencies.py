

from fastapi import HTTPException

def get_session_token(token: str):
    valid_token = "FHXIKD"
    if token != valid_token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

