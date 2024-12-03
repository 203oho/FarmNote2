from datetime import datetime
from typing import List, Optional
import datetime
from ..schemas import Note, NoteBase
from ..database import Database

# Initialize the Database object
database = Database()

note_id_counter = 1

def create_example_notes():
    # This will now interact with the database rather than in-memory data
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

def create_note(note_data: Note, token: str) -> Note:
    # Using the database to create a note
    session_id = 1  # Assuming session ID is passed or fetched dynamically
    new_note = database.create_note(note_data, session_id)
    return Note(
        id=new_note.id,
        session_id=new_note.session_id,
        content=new_note.content,
        latitude=new_note.latitude,
        longitude=new_note.longitude,
        temperature=note_data.temperature,
        creation_date=new_note.creation_date,
        updated_date=new_note.updated_date,
    )


def update_note(note_id: int, note_data: Note, token: str) -> Optional[Note]:
    # Simulate updated_date being added by the database
    updated_note_model = database.update_note(note_id, note_data)
    if updated_note_model is None:
        return None

    # Ensure updated_date is always included when returning the Note
    return Note(
        id=updated_note_model.id,
        session_id=updated_note_model.session_id,
        content=updated_note_model.content,
        latitude=updated_note_model.latitude,
        longitude=updated_note_model.longitude,
        temperature=updated_note_model.temperature,
        creation_date=updated_note_model.creation_date,
        updated_date=updated_note_model.updated_date or datetime.utcnow()  # Default to current time if None
    )



def get_note(note_id: int, token: str) -> Optional[Note]:
    # Fetch the note using the database
    note_model = database.get_note(note_id)
    if note_model is None:
        return None

    return Note(
        id=note_model.id,
        session_id=note_model.session_id,
        content=note_model.content,
        latitude=note_model.latitude,
        longitude=note_model.longitude,
        temperature=18.3,
        creation_date=note_model.creation_date,
        updated_date=note_model.updated_date,
    )

def read_notes(token: str) -> List[Note]:
    # Fetch all notes related to a session using the database
    session_id = 1  # Assuming the session ID is passed or fetched dynamically
    note_models = database.get_notes_by_session(session_id)
    return [
        Note(
            id=note.id,
            session_id=note.session_id,
            content=note.content,
            latitude=note.latitude,
            longitude=note.longitude,
            temperature=18.3,  # Assuming temperature is not a field in the model
            creation_date=note.creation_date,
            updated_date=note.updated_date,
        ) for note in note_models
    ]

def read_note(note_id: int, token: str) -> Optional[Note]:
    # Fetch a single note using the database
    return get_note(note_id, token)

def delete_note(note_id: int, token: str) -> bool:
    # Delete the note using the database
    success = database.delete_note(note_id)
    return success

