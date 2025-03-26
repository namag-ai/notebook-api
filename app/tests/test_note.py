from pydoc import cli
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import collection
from bson import ObjectId
from app.schemas.note import individual_note, all_notes

client = TestClient(app)


# Test cases for individual_note
def test_individual_note_valid_input():
    note = {"_id": 1, "title": "Test Title", "description": "Test Description"}
    result = individual_note(note)
    assert result == {"id": "1", "title": "Test Title", "description": "Test Description"}

def test_individual_note_missing_id():
    note = {"title": "Test Title", "description": "Test Description"}
    with pytest.raises(KeyError):
        individual_note(note)

def test_individual_note_missing_title():
    note = {"_id": 1, "description": "Test Description"}
    with pytest.raises(KeyError):
        individual_note(note)

def test_individual_note_missing_description():
    note = {"_id": 1, "title": "Test Title"}
    with pytest.raises(KeyError):
        individual_note(note)

def test_individual_note_empty_input():
    note = {}
    with pytest.raises(KeyError):
        individual_note(note)

def test_individual_note_id_as_string():
    note = {"_id": "123", "title": "Test Title", "description": "Test Description"}
    result = individual_note(note)
    assert result == {"id": "123", "title": "Test Title", "description": "Test Description"}

def test_individual_note_extra_fields():
    note = {"_id": 1, "title": "Test Title", "description": "Test Description", "extra": "Extra Field"}
    result = individual_note(note)
    assert result == {"id": "1", "title": "Test Title", "description": "Test Description"}

# Test cases for all_notes
def test_all_notes_valid_input():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1"},
        {"_id": 2, "title": "Title 2", "description": "Description 2"},
    ]
    result = all_notes(notes)
    assert result == [
        {"id": "1", "title": "Title 1", "description": "Description 1"},
        {"id": "2", "title": "Title 2", "description": "Description 2"},
    ]

def test_all_notes_empty_list():
    notes = []
    result = all_notes(notes)
    assert result == []

def test_all_notes_single_note():
    notes = [{"_id": 1, "title": "Title 1", "description": "Description 1"}]
    result = all_notes(notes)
    assert result == [{"id": "1", "title": "Title 1", "description": "Description 1"}]

def test_all_notes_missing_id_in_one_note():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1"},
        {"title": "Title 2", "description": "Description 2"},
    ]
    with pytest.raises(KeyError):
        all_notes(notes)

def test_all_notes_missing_title_in_one_note():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1"},
        {"_id": 2, "description": "Description 2"},
    ]
    with pytest.raises(KeyError):
        all_notes(notes)

def test_all_notes_missing_description_in_one_note():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1"},
        {"_id": 2, "title": "Title 2"},
    ]
    with pytest.raises(KeyError):
        all_notes(notes)

def test_all_notes_extra_fields_in_notes():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1", "extra": "Extra Field"},
        {"_id": 2, "title": "Title 2", "description": "Description 2"},
    ]
    result = all_notes(notes)
    assert result == [
        {"id": "1", "title": "Title 1", "description": "Description 1"},
        {"id": "2", "title": "Title 2", "description": "Description 2"},
    ]

def test_all_notes_id_as_string():
    notes = [
        {"_id": "1", "title": "Title 1", "description": "Description 1"},
        {"_id": "2", "title": "Title 2", "description": "Description 2"},
    ]
    result = all_notes(notes)
    assert result == [
        {"id": "1", "title": "Title 1", "description": "Description 1"},
        {"id": "2", "title": "Title 2", "description": "Description 2"},
    ]

def test_all_notes_mixed_id_types():
    notes = [
        {"_id": 1, "title": "Title 1", "description": "Description 1"},
        {"_id": "2", "title": "Title 2", "description": "Description 2"},
    ]
    result = all_notes(notes)
    assert result == [
        {"id": "1", "title": "Title 1", "description": "Description 1"},
        {"id": "2", "title": "Title 2", "description": "Description 2"},
    ]

@pytest.mark.asyncio
async def test_get_all_notes():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_post_note_success():
    note_data = {"id":"test", "title": "Test Note", "description": "This is a test note."}
    response = client.post("/", json=note_data)
    assert response.status_code == 201
    assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_post_note_failure():
    response = client.post("/", json={})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_update_note_success():
    note_id = client.get("/").json()[0]["id"]
    updated_data = {"id":"test", "title": "Updated Title", "description": "Updated description."}
    response = client.put(f"/{note_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_update_note_not_found():
    note_id = "66123abc456789def0000000"
    updated_data = {"title": "New Title", "description": "New Description"}
    response = client.put(f"/{note_id}", json=updated_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_delete_note_success():
    note_id = client.get("/").json()[0]["id"]
    print("Hello", note_id)
    response = client.delete(f"/{note_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_delete_note_not_found():
    note_id = "77123abc456789def0000110"
    response = client.delete(f"/{note_id}")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_notes_returns_list():
    response = client.get("/")
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_post_note_without_title():
    note_data = {"description": "Missing title."}
    response = client.post("/", json=note_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_post_note_without_description():
    note_data = {"title": "Missing description."}
    response = client.post("/", json=note_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_update_note_with_invalid_id():
    invalid_id = "not_a_valid_id"
    updated_data = {"title": "Invalid ID", "description": "Test description"}
    response = client.put(f"/{invalid_id}", json=updated_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_delete_note_with_invalid_id():
    note_id = "67e3b1cf0ef1e015f07305bc"
    response = client.delete(f"/{note_id}")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_post_duplicate_note():
    note_data = {"id":"test", "title": "Duplicate Note", "description": "This is a duplicate."}
    client.post("/", json=note_data)
    response = client.post("/", json=note_data)
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_post_empty_body():
    response = client.post("/", json={})
    assert response.status_code == 422
