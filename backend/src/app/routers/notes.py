from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
import uuid

from app import schemas
from app.schemas import Note,NoteCreate
from app.dependencies import get_session_token

router = APIRouter(prefix="/notes", tags=["notes"])

# Temporary in-memory storage for notes, keyed by session token
__FAKE_DB_NOTES = {}


@router.post(
    "/",
    response_model=Note,
    operation_id="createNote",
    description="Create a new note in the session.",
)
def create_note(note: NoteCreate, token: str = Depends(get_session_token)):
    if token not in __FAKE_DB_NOTES:
        __FAKE_DB_NOTES[token] = []

    # Generate a new note with a unique ID and current timestamp
    new_note = Note(
        id=str(uuid.uuid4()),
        title=note.title,
        content=note.content,
        location=note.location,
        category=note.category,
        created_at=datetime.now(),
    )

    __FAKE_DB_NOTES[token].append(new_note)
    return new_note


@router.get(
    "/",
    response_model=List[Note],
    operation_id="readNotes",
    description="Return all notes of an existing session.",
)
def read_notes(token: str = Depends(get_session_token)):
    return __FAKE_DB_NOTES.get(token, [])


@router.get(
    "/{note_id}",
    response_model=Note,
    operation_id="readNote",
    description="Get a single note by its ID.",
)
def read_note(note_id: str, token: str = Depends(get_session_token)):
    notes = __FAKE_DB_NOTES.get(token, [])
    for note in notes:
        if note.id == note_id:
            return note
    note_not_found_error()


@router.put(
    "/{note_id}",
    response_model=Note,
    operation_id="updateNote",
    description="Update an existing note by its ID.",
)
def update_note(note_id: str, updated_note: schemas.NoteCreate, token: str = Depends(get_session_token)):
    notes = __FAKE_DB_NOTES.get(token, [])
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = Note(
                id=note.id,
                title=updated_note.title,
                content=updated_note.content,
                location=updated_note.location,
                category=updated_note.category,
                created_at=note.created_at
            )
            return notes[index]
    note_not_found_error()


@router.delete(
    "/{note_id}",
    operation_id="deleteNote",
    description="Delete a note by its ID.",
)
def delete_note(note_id: str, token: str = Depends(get_session_token)):
    notes = __FAKE_DB_NOTES.get(token, [])
    for index, note in enumerate(notes):
        if note.id == note_id:
            del notes[index]
            return {"message": "Note deleted successfully"}
    note_not_found_error()


def note_not_found_error():
    raise HTTPException(status_code=404, detail="Note not found.")

def invalid_data_error():
    raise HTTPException(status_code=422, detail="Invalid data provided.")



