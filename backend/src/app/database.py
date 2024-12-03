from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.models import Base, SessionModel, NoteModel


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
        if session:
            note.session_id = session.id
            self.session.add(note)
            self.session.commit()
            return note
        return None

    def get_notes_by_token(self, token: str):
        session = self.get_session_by_token(token)
        if session:
            return self.session.query(NoteModel).filter_by(session_id=session.id).all()
        return None

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