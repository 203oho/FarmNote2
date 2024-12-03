from datetime import datetime
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.dbnotemodel import SessionModel, NoteModel, Base
from app.schemas import Note
from sqlalchemy.orm import Session
from fastapi import HTTPException


class Database:
    def __init__(self, db_url='sqlite:///notes.db'):
        """Initialize the database engine and session maker."""
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)  # Create all tables based on models
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        """Get a new session for interacting with the database."""
        return self.Session()

    def create_sesh(self, token: str) -> None:
        """Create a new session for a given token."""
        with self.get_session() as session:
            # Check if the session already exists
            existing_session = session.query(SessionModel).filter(SessionModel.token == token).first()
            if existing_session:
                print(f"DB: Session with token {token} already exists")
                return  # If the session already exists, we do nothing
            new_session = SessionModel(token=token)
            session.add(new_session)
            session.commit()
            print(f"DB: created session with token {token}")

    def create_note(self, note_data: Note, session_id: int) -> NoteModel:
        """Create a new note in the database."""
        with self.get_session() as session:
            new_note = NoteModel(
                session_id=session_id,
                content=note_data.content,
                latitude=note_data.latitude,
                longitude=note_data.longitude,
                creation_date=datetime.now(),
                updated_date=datetime.now(),
                temperature=note_data.temperature,
            )
            session.add(new_note)
            session.commit()
            session.refresh(new_note)  # Ensure the note has been added and returned with an ID
            print(f"DB: created note with ID {new_note.id}")
            return new_note

    def update_note(self, note_id: int, note_data: Note) -> NoteModel:
        """Update an existing note in the database."""
        with self.get_session() as session:
            note = session.query(NoteModel).filter(NoteModel.id == note_id).first()
            if not note:
                raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found")

            note.content = note_data.content or note.content
            note.temperature = note_data.temperature or note.temperature
            note.latitude = note_data.latitude or note.latitude
            note.longitude = note_data.longitude or note.longitude
            note.updated_date = note_data.updated_date or datetime.now()  # Ensure we set a valid updated date

            session.commit()
            session.refresh(note)  # Get the updated note
            print(f"DB: updated note with ID {note.id}")
            return note

    def get_note(self, note_id: int) -> NoteModel:
        """Get a note by its ID."""
        with self.get_session() as session:
            note = session.query(NoteModel).filter(NoteModel.id == note_id).first()
            if note:
                print(f"DB: retrieved note with ID {note.id}")
            else:
                print(f"DB: Note with ID {note_id} not found")
            return note

    def get_notes_by_session(self, session_id: int) -> List[NoteModel]:
        """Get all notes for a specific session."""
        with self.get_session() as session:
            notes = session.query(NoteModel).filter(NoteModel.session_id == session_id).all()
            print(f"DB: retrieved {len(notes)} notes for session {session_id}")
            return notes

    def delete_note(self, note_id: int) -> bool:
        """Delete a note by its ID."""
        with self.get_session() as session:
            note = session.query(NoteModel).filter(NoteModel.id == note_id).first()
            if note:
                session.delete(note)
                session.commit()
                print(f"DB: deleted note with ID {note_id}")
                return True
            else:
                print(f"DB: Note with ID {note_id} not found")
                return False
