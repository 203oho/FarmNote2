
from datetime import datetime
from typing import List, Optional
from app.schemas.note import Note, NoteBase

# Temporary in-memory database
__FAKE_DB_NOTES = []

def create_note(note_data: NoteBase) -> Note:
    new_note = Note(
        id=len(__FAKE_DB_NOTES),  # using the current list length as a simple ID generator
        session_id=1,
        content=note_data.content,
        latitude=note_data.latitude,
        longitude=note_data.longitude,
        temperature=note_data.temperature,
        creation_date=datetime.utcnow(),
        updated_date=datetime.utcnow(),
    )
    __FAKE_DB_NOTES.append(new_note)
    return new_note

def read_notes() -> List[Note]:
    return [note for note in __FAKE_DB_NOTES]

def read_note(note_id: int) -> Optional[Note]:
    for note in __FAKE_DB_NOTES:
        if note.id == note_id:
            return note
    return None

def get_note(note_id: int):
    return find_my_note_by_id(note_id)

def find_my_note_by_id(note_id: int):
    return next((note for note in __FAKE_DB_NOTES if note.id == note_id), None)

def update_note(note_id: int, updated_data: NoteBase) -> Optional[Note]:
    for index, note in enumerate(__FAKE_DB_NOTES):
        if note.id == note_id:
            updated_note = Note(
                id=note.id,
                session_id=note.session_id,
                content=updated_data.content or note.content,
                latitude=updated_data.latitude or note.latitude,
                longitude=updated_data.longitude or note.longitude,
                temperature=updated_data.temperature or note.temperature,
                creation_date=note.creation_date,
                updated_date=datetime.utcnow(),
            )
            __FAKE_DB_NOTES[index] = updated_note
            return updated_note
    return None

def delete_note(note_id: int):
    note = find_my_note_by_id(note_id)
    if note is None:
        return False

    global __FAKE_DB_NOTES
    __FAKE_DB_NOTES= [n for n in __FAKE_DB_NOTES if n.id != note_id]
    return True
