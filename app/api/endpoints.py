from unittest import result
from fastapi import APIRouter
from models.note import Note
from db.session import collection
from schemas.note import all_notes, individual_note
from bson import ObjectId

router = APIRouter()

# GET all the notes
@router.get("/")
async def get_notes():
    notes = all_notes(collection.find())
    return notes

# POST new notes
@router.post("/")
async def post_note(note: Note):
    result = collection.insert_one(dict(note))

    if result.acknowledged:
        return {"status": "success", "status_code": 201,  "message": "Note added successfully"}
    else:
        return {"status": "failure", "status_code": 500, "message": "Failed to add note"}

# Update notes
@router.put("/{id}")
async def update_note(id:str, note:Note):
    result = collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(note)})
    if result:
        return {"status": "success", "status_code": 200, "message": "Note updated successfully"}
    else:
        return {"status": "failure", "status_code": 500, "message": "Failed to update note"}

# Delete notes
@router.delete("/{id}")
async def delete_note(id:str, note:Note):
    result = collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"status": "success", "status_code": 200, "message": "Note deleted successfully"}
    else:
        return {"status": "failure", "status_code": 500, "message": "Failed to delete note"}
