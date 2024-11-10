from datetime import datetime
from typing import List, Optional
import datetime
from ..schemas import NoteBase, Note

# Initialize __FAKE_DB_NOTES as a dictionary with tokens as keys
__FAKE_DB_NOTES = {
    "token1": [],
    "token2": [],
}
note_id_counter = 1


def create_example_notes():
    """
    Return a list of example notes.
    """
    notes = [
        Note(
            id=0,
            session_id=0,
            content='Hello World',
            latitude=48.1271,
            longitude=15.1247,
            temperature=15.3,
            creation_date=datetime.datetime.utcnow(),
            updated_date=datetime.datetime.utcnow(),
        ),
        Note(
            id=1,
            session_id=0,
            content='Example Note 2',
            latitude=48.21,
            longitude=15.125,
            temperature=18.3,
            creation_date=datetime.datetime.utcnow(),
            updated_date=datetime.datetime.utcnow(),
        )
    ]
    return notes


def create_note(note_data: NoteBase, token: str) -> Note:
    global note_id_counter

    # Ensure the token key exists in the fake database
    if token not in __FAKE_DB_NOTES:
        __FAKE_DB_NOTES[token] = []

    new_note = Note(
        id=note_id_counter,
        session_id=1,
        content=note_data.content,
        latitude=note_data.latitude,
        longitude=note_data.longitude,
        temperature=note_data.temperature,
        creation_date=datetime.datetime.now(),
        updated_date=datetime.datetime.now(),
    )

    __FAKE_DB_NOTES[token].append(new_note)
    note_id_counter += 1
    return new_note


def read_notes(token: str) -> list:
    return __FAKE_DB_NOTES.get(token, [])  # Return an empty list if the token is not found


def get_note(note_id: int, token: str) -> Optional[Note]:
    return next((note for note in __FAKE_DB_NOTES.get(token, []) if note.id == note_id), None)


def read_note(note_id: int, token: str) -> Optional[Note]:
    return get_note(note_id, token)


def update_note(note_id: int, updated_note_data: NoteBase, token: str) -> Optional[Note]:
    note = get_note(note_id, token)
    if note is None:
        return None


    note.content = updated_note_data.content or note.content
    note.latitude = updated_note_data.latitude or note.latitude
    note.longitude = updated_note_data.longitude or note.longitude
    note.temperature = updated_note_data.temperature or note.temperature
    note.updated_date = datetime.datetime.now()

    return note


def delete_note(note_id: int, token: str) -> bool:
    note = get_note(note_id, token)
    if note is None:
        return False

    __FAKE_DB_NOTES[token] = [n for n in __FAKE_DB_NOTES[token] if n.id != note_id]
    return True
