from fastapi import APIRouter, HTTPException, Depends
from app import schemas, usecases, dependencies

router = APIRouter(
    prefix='/session',
    tags=['session'],
)


@router.post("/", response_model=schemas.Session, operation_id='getNewSession', description='Request a new session')
def create_session():
    token = schemas.get_a_session_token()
    session = usecases.create_session(token)
    return schemas.Session.from_orm(session)


@router.post("/join/{token}", operation_id='joinSession', description='join a session and return all notes from the session')
def join_session(token: str):
    notes= usecases.join_session(token)
    return notes



@router.get("/", response_model=schemas.Session, operation_id='getSession', description='get a session by ID')
def get_session():
    noteSession = usecases.get_session()
    if noteSession is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return noteSession