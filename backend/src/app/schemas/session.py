from pydantic import BaseModel

class Session(BaseModel):
    id: int
    token: str

    class Config:
        orm_mode = True
        from_attributes = True