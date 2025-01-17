from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.models import Base, SessionModel, NoteModel
from app.schemas import Session

def de_database_ify(note: NoteModel | None) -> dict:
    return {
        "id": note.id,
        "session_id": note.session_id,
        "content": note.content,
        "latitude": note.latitude,
        "longitude": note.longitude,
        "creation_date": note.creation_date,
        "updated_date": note.updated_date,
        "temperature": note.temperature
    } if note is not None else None

class Database:
    def __init__(self):
        self.engine = create_engine(settings.database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_session(self, token: str):
        new_session = SessionModel(token=token)
        self.session.add(new_session)
        self.session.commit()
        print(f"Session created; Token: {token}")
        return new_session


    def join_session(self, token: str):
        session_id= self.session.query(SessionModel.id)
        session = self.session.query(SessionModel).filter_by(token=token).first()
        if session is None:
            return None
        notes = self.session.query(NoteModel).filter(NoteModel.session_id == session_id).all()
        return notes

    def get_sessions(self):
        session = self.session.query(SessionModel).all()
        return [Session.Session(id=ses.id, token=ses.token) for ses in session]

    def get_session_by_token(self, token: str):
        return self.session.query(SessionModel).filter_by(token=token).first()

    def delete_session_logic(self, session_id: int):
        session_to_delete = self.session.query(SessionModel).filter_by(id=session_id).first()

        if not session_to_delete:
            return False

        notes = self.session.query(NoteModel).filter_by(session_id=session_id).all()
        for note in notes:
            self.session.delete(note)

        self.session.delete(session_to_delete)
        self.session.commit()

        return True

    def add_note_to_session(self, note: NoteModel, token: str):
        session = self.get_session_by_token(token)
        print(note)
        if session:
            note.session_id = session.id
            self.session.add(note)
            self.session.commit()
            return note
        return None

    def get_notes_by_token(self, token: str):
        print("token", token)
        session = self.get_session_by_token(token)
        print("Herbert",session)
        if session:
            print(self.session.query(NoteModel).filter_by(session_id=session.id).all())

            notes = self.session.query(NoteModel).filter_by(session_id=session.id).all()
            return [de_database_ify(note) for note in notes]

    def get_note_by_id_and_token(self, note_id: int, token: str):
        session = self.get_session_by_token(token)
        if session:
            return self.session.query(NoteModel).filter_by(id=note_id, session_id=session.id).first()
        return None

    def update_note(self, note: NoteModel):
        self.session.commit()


    def delete_note_by_id_and_token(self, note_id: int, token: str):
        note = self.get_note_by_id_and_token(note_id, token)
        if note:
            self.session.delete(note)
            self.session.commit()
            return True
        return False

    def get_sessions(self):
        sessions = self.session.query(SessionModel).all()  # Abrufen aller Sessions
        print(sessions)  # Debugging: Gibt die abgerufenen Sessions aus
        return [Session(id=int(str(ses.id)), token=str(ses.token)) for ses in sessions]