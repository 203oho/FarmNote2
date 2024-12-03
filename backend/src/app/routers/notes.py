from typing import List
from fastapi import APIRouter, Depends, HTTPException
from .. import dependencies, usecases
from ..schemas import NoteBase, Note

router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)

@router.post("/", response_model=Note, operation_id='createNote', description='Create a new note')
def create_note(note: NoteBase, token: str = Depends(dependencies.get_session_token)):
    new_note = usecases.create_note(note, token)
    if new_note is None:
        raise HTTPException(status_code=422, detail="Invalid input data.")
    return new_note

@router.get("/", response_model=List[Note], operation_id='readNotes', description='Return all notes.')
def read_notes(token: str = Depends(dependencies.get_session_token)):
    try:
        notes = usecases.read_notes(token)
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve notes")


@router.get("/{note_id}", response_model=Note, operation_id='getNote', description='Get note by ID.')
def get_note_by_id(note_id: int, token: str = Depends(dependencies.get_session_token)):
    note = usecases.get_note(note_id,token)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=Note, operation_id='updateNote', description='Update an existing note.')
def update_note(note_id: int, note: NoteBase, token: str = Depends(dependencies.get_session_token)):
    updated_note = usecases.update_note(note_id, note,token)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/{note_id}", operation_id='deleteNote', description='Delete a note by ID.')
def delete_note(note_id: int, token: str = Depends(dependencies.get_session_token)):
    success = usecases.delete_note(note_id,token)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
