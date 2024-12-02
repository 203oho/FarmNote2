from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime

# Define the base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Define the NoteModel
class NoteModel(Base):
    __tablename__ = 'notes'  # Correct the table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('sessions.index'), nullable=False)  # ForeignKey to sessions table
    creation_date = Column(DateTime, default=datetime.utcnow)  # Set default to current time
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Automatically updated
    latitude = Column(Float)
    longitude = Column(Float)
    content = Column(String, nullable=False)  # Ensure content is required

    # Define the relationship to SessionModel
    session = relationship('SessionModel', back_populates='notes')  # Assuming back_populates is defined in SessionModel


# Define the SessionModel
class SessionModel(Base):
    __tablename__ = 'sessions'  # Define the sessions table

    index = Column(Integer, primary_key=True, autoincrement=True)  # Primary key for the session
    session_name = Column(String, nullable=False)  # A field to represent the session's name or other data

    # Define the relationship to NoteModel
    notes = relationship('NoteModel', back_populates='session')  # Connect notes to session (bidirectional)


