from typing import List
from fastapi import APIRouter, Depends, HTTPException
from .. import dependencies, usecases
from ..schemas import NoteBase, Note
import logging

router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)

# Set up logging
logger = logging.getLogger(__name__)

@router.post("/", response_model=Note, operation_id='createNote')
def create_note(note: NoteBase, token: str = Depends(dependencies.get_session_token)):
    new_note = usecases.create_note(note)
    if new_note is None:
        logger.error("Failed to create note: Note creation returned None.")
        raise HTTPException(status_code=500, detail="Failed to create note")
    return new_note

@router.get("/", response_model=List[Note], operation_id='readNotes', description='Return all notes.')
def read_notes(token: str = Depends(dependencies.get_session_token)):
    try:
        notes = usecases.read_notes()
        return notes
    except Exception as e:
        logger.exception(f"An error occurred while reading notes for token: {token}")
        raise HTTPException(status_code=404, detail="Note not found")


@router.get("/{note_id}", response_model=Note, operation_id='getNote', description='Get note by ID.')
def get_note_by_id(note_id: int, token: str = Depends(dependencies.get_session_token)):
    note = usecases.get_note(note_id)  # Ensure this points to the correct function
    if note is None:
        logger.warning(f"Note with ID {note_id} not found.")
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=Note, operation_id='updateNote', description='Update an existing note.')
def update_note(note_id: int, note: NoteBase, token: str = Depends(dependencies.get_session_token)):
    updated_note = usecases.update_note(note_id, note)
    if updated_note is None:
        logger.warning(f"Attempted to update non-existing note with ID {note_id}.")
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/{note_id}", operation_id='deleteNote', description='Delete a note by ID.')
def delete_note(note_id: int, token: str = Depends(dependencies.get_session_token)):
    success = usecases.delete_note(note_id)
    if not success:
        logger.warning(f"Attempted to delete non-existing note with ID {note_id}.")
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}