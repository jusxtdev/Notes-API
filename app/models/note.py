from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.base import Base

class Note(Base):
    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String)

    created_at = Column(DateTime, default=datetime.now())

    # FOreign key - user_id
    user_id = Column(Integer, ForeignKey('users.id'))

    # many to one relationship
    user = relationship('User', back_populates='notes')