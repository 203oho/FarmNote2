from fastapi import APIRouter, HTTPException, Depends, WebSocket
from starlette.responses import StreamingResponse


from app import schemas, usecases, dependencies, config
from ..qr_code import generate_qr_code

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


@router.get("/qrcode", operation_id='getSessionQRCode', description='Get a QR code for the specified session')
def get_session_qrcode(token: str):
    session = usecases.get_session_by_token(token)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    qr_url = config.settings.qr_code_url.format(frontend_url=config.settings.frontend_url, token=session.token)
    buffer = generate_qr_code(qr_url)

    return StreamingResponse(buffer, media_type="image/png")
