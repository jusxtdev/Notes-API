from pydantic import BaseModel
from datetime import datetime

class Note(BaseModel):
    note_id : int
    content : str
    createdAt : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def fetch_id(self):
        return self.note_id