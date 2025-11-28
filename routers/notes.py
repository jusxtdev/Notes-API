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

    # Operation
    note.note_id = len(data)
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
    matched_id = match_id(note_id=note_id, data=data)
    if matched_id is None:
        content = {'success' : False,'message' : 'Invalid note Id'}
        content = jsonable_encoder(content)
        return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND)
    else:
        deleted = data.pop(matched_id)
        content = {'success':True,'deleted note': deleted}
        content = jsonable_encoder(content)
        return  JSONResponse(content=content, status_code=status.HTTP_200_OK)
    
# TODO - Fix the delete pop index error
'''
your are directly deletein object through matched_id, which deletes that index but not the object with that index
'''


# -----------   Utility Functions   --------------------
def match_id(note_id : int, data:list[Note]):
    for note_obj in data:
        note_obj_id = note_obj.fetch_id()
        if note_obj_id == note_id:
            return note_obj_id
    return None