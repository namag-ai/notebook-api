from fastapi import APIRouter
from app.models.note import Note
from app.db.session import collection
from app.schemas.note import all_notes, individual_note
from bson import ObjectId
from fastapi.responses import JSONResponse


router = APIRouter()

# GET all the notes
@router.get("/")
async def get_notes():
    notes = all_notes(collection.find())
    return notes

# Get ine note
@router.get("/{id}")
async def get_one_note(id:str):
    note = individual_note(collection.find_one({"_id": ObjectId(id)}))
    return note

# POST new notes
@router.post("/")
async def post_note(note: Note):
    result = collection.insert_one(dict(note))

    if result.acknowledged:
        return JSONResponse(content={"status": "success", "message": "Note added successfully"}, status_code=201)
    else:
        return JSONResponse(content={"status": "failure", "message": "Failed to add note"}, status_code=400)

# Update notes
@router.put("/{id}")
async def update_note(id:str, note:Note):
    result = collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(note)})
    if result:
        updated_note = collection.find_one({"_id": ObjectId(id)})
        if any(value is None for value in updated_note.values()):
            return JSONResponse(content={"status": "failure", "message": "Update resulted in null field value"}, status_code=400)
        return JSONResponse(content={"status": "success", "message": "Note updated successfully"}, status_code=200)
    else:
        return JSONResponse(content={"status": "failure", "message": "Failed to update note"}, status_code=404)

# Delete notes
@router.delete("/{id}")
async def delete_note(id:str):
    result = collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return JSONResponse(content={"status": "success", "message": "Note deleted successfully"}, status_code=200)
    else:
        return JSONResponse(content={"status": "failure", "message": "Failed to delete note"}, status_code=404)
