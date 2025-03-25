def individual_note(note)->dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "description": note["description"],
    }

def all_notes(notes)->list:
    all_notes = [individual_note(note) for note in notes]
    return all_notes