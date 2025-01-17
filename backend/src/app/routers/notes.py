from typing import List
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from app import dependencies, usecases
from app.database import Database
from app.schemas import NoteBase, Note


router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)

db = Database()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@router.post("/", response_model=Note, operation_id='createNote', description='Create a new note')
async def create_note(note: NoteBase, token: str = Depends(dependencies.validation_token)):
    new_note = usecases.create_note(note, token)

    if new_note is None:
        raise HTTPException(status_code=422, detail="Invalid input data.")

    message = {"action": "created", "noteId": new_note.id}
    await manager.broadcast(message)

    return new_note

@router.get("/", response_model=List[Note], operation_id='readNotes', description='Return all notes.')
def read_notes(token: str = Depends(dependencies.validation_token)):
    print(token, "id")
    try:
        notes = usecases.read_notes(token)
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve notes")


@router.get("/{note_id}", response_model=Note, operation_id='getNote', description='Get note by ID.')
def read_note(note_id: int, token: str = Depends(dependencies.validation_token)):
    note = usecases.read_note(note_id,token)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=Note, operation_id='updateNote', description='Update an existing note.')
async def update_note(note_id: int, note: NoteBase, token: str = Depends(dependencies.validation_token)):
    updated_note = usecases.update_note(note_id, note,token)

    # WebSocket Broadcast
    message = {"action": "updated", "noteId": updated_note.id}
    await manager.broadcast(message)

    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/{note_id}", operation_id='deleteNote', description='Delete a note by ID.')
async def delete_note(note_id: int, token: str = Depends(dependencies.validation_token)):
    success = usecases.delete_note(note_id,token)

    # WebSocket Broadcast
    if success:
        message = {"action": "deleted", "noteId": note_id}
        await manager.broadcast(message)

    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}



@router.websocket("/ws",name="Websocket")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
