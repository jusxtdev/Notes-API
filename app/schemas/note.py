'''
Contains Schema for Note object
'''

from pydantic import BaseModel
from datetime import datetime

class Note(BaseModel):
    note_id : int
    content : str
    createdAt : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def fetch_id(self):
        return self.note_id
    
class NoteCreate(BaseModel):
    title : str
    content : str | None = None

class NoteResponse(BaseModel):
    note_id : int
    title : str
    content : str | None
    user_id : int | None

    model_config = {"from_attributes" : True}