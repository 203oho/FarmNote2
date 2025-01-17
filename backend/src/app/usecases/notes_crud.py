import datetime
from app.models import NoteModel
from app.database import Database
from app.schemas import NoteBase

db=Database()

def create_note(note_data: NoteBase, token: str):
    session_exists_by_token(token)  # Ensure session exists
    note = NoteModel(
        content=note_data.content,
        latitude=note_data.latitude,
        longitude=note_data.longitude,
        temperature=note_data.temperature,
        creation_date=datetime.datetime.now(),
        updated_date=datetime.datetime.now(),
    )
    return db.add_note_to_session(note, token)


def read_notes(token: str):
    return db.get_notes_by_token(token)

def read_note(note_id: int, token: str):
    session = session_exists_by_token(token)  # Ensure session exists
    return db.get_note_by_id_and_token(note_id, session.token)

def update_note(note_id: int, updated_note_data: NoteBase, token: str):
    session = session_exists_by_token(token)
    note = db.get_note_by_id_and_token(note_id, session.token)
    if note:
        note.content = updated_note_data.content
        note.latitude = updated_note_data.latitude
        note.longitude = updated_note_data.longitude
        note.updated_date = datetime.datetime.now()
        note.temperature = updated_note_data.temperature
        db.update_note(note)
        return note
    return None

def delete_note(note_id: int, token: str):
    session = session_exists_by_token(token)  # Ensure session exists
    return db.delete_note_by_id_and_token(note_id, session.token)

def create_session(token: str):
    session = db.create_session(token)
    return session

def get_session():
    return db.get_session()

def join_session(token: str):
    return db.join_session(token)


def get_session_by_token(token: str):
    noteSessions = db.get_session_by_token(token)
    return noteSessions


def session_exists_by_token(token: str):
    noteSession = db.get_session_by_token(token)
    if not noteSession:
        db.create_session(token)
        noteSession = db.get_session_by_token(token)
    return noteSession


def delete_session(token: str):
    session_to_delete = db.get_session_by_token(token)

    if not session_to_delete:
        return False

    notes = db.get_notes_by_token(token)
    if notes:
        for note in notes:
            db.delete_note_by_id_and_token(note.id, token)

    success = db.delete_session_logic(session_to_delete)

    return success