from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.note import Note
from data import data

router = APIRouter(
    prefix='/api',
    tags=['NotesAPI']
    )

# -----------   POST Routes   --------------------

@router.post('/notes')
def add_note(note : Note):

    # indexing
    if len(data) == 0:
        note.note_id = 0
    else:
        latest_obj = data[-1]
        latest_obj_id = latest_obj.fetch_id()
        note.note_id = latest_obj_id + 1


    data.append(note)

    # Return
    content =  {
        'received' : note.model_dump(),
        'response' : data
    }
    content = jsonable_encoder(content)
    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)


# -----------   GET Routes   --------------------


@router.get('/api/notes')
def get_notes():
    content = {
        'success' : True,
        'response' : data
        }
    content = jsonable_encoder(content)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@router.get('/api/notes/{note_id}')
def get_note_by_id(note_id : int):
    matched_id = match_id(note_id, data)
    if matched_id is None:
        content = {
            'success' : False,
            'message' : 'Invalid note Id'
            }
        content = jsonable_encoder(content)
        return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND) 
    else:
        content = {
            'success':True,
            'response' : data[matched_id]
            }
        content = jsonable_encoder(content)
        return JSONResponse(content=content, status_code=status.HTTP_200_OK)

 
# -----------   PUT Routes   --------------------


@router.put('/api/notes/{note_id}')
def update_note(note_id : int, update_data : Note):
    matched_id = match_id(note_id, data)
    if matched_id is None:
        content = {
            'success' : False,
            'message' : 'Invalid note Id'}
        content = jsonable_encoder(content)
        return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND) 
    else:
        existing_note = data[matched_id]
        new_content = update_data.content
        existing_note.content = new_content
        data[matched_id] = existing_note
        content = jsonable_encoder(data[matched_id])
        return JSONResponse(content=content, status_code=status.HTTP_200_OK)
    

# -----------   DELETE Routes   --------------------


@router.delete('/api/notes/{note_id}')
def delete_note(note_id : int):
    matched_obj = fetch_obj(note_id=note_id, data=data)
    if matched_obj is None:
        content = {'success' : False,'message' : 'Invalid note Id'}
        content = jsonable_encoder(content)
        return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND)
    else:
        data.remove(matched_obj)
        content = {'success':True,'deleted note': matched_obj}
        content = jsonable_encoder(content)
        return  JSONResponse(content=content, status_code=status.HTTP_200_OK)
    

# -----------   Utility Functions   --------------------
def match_id(note_id : int, data:list[Note]):
    for note_obj in data:
        note_obj_id = note_obj.fetch_id()
        if note_obj_id == note_id:
            return note_obj_id
    return None

def fetch_obj(note_id : int, data : list[Note]):
    for note_obj in data:
        note_obj_id = note_obj.fetch_id()
        if note_obj_id == note_id:
            return note_obj
    return None