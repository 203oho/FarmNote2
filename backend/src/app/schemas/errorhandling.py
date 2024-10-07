from fastapi import HTTPException

def note_not_found_error():
    raise HTTPException(status_code=404, detail="Note not found.")

def invalid_data_error():
    raise HTTPException(status_code=422, detail="Invalid data provided.")
