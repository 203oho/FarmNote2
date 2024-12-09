

from fastapi import HTTPException

def validation_token(token: str):
    if token is None or token in '123456789':
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

