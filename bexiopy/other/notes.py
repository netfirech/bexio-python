from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.api.models import DeleteResponse
from bexiopy.other.models import Note, NoteSearch, NotePost


def get_notes() -> List[Note]:
    client = BexioAPIClient()
    response = client.get('/note')
    return parse_obj_as(List[Note], response)


def get_note(note_id: int) -> Note:
    client = BexioAPIClient()
    response = client.get(f'/note/{note_id}')
    return parse_obj_as(Note, response)


def create_note(note: NotePost) -> Note:
    client = BexioAPIClient()
    response = client.post('/note', note.dict())
    return parse_obj_as(Note, response)


def edit_note(note: Note) -> Note:
    client = BexioAPIClient()

    # Mapping between the Note and NotePost schema.
    # This needs to be done until Bexio fixed the inconsistency in their /note endpoint
    post_note: NotePost = NotePost(
        id=note.id,
        user_id=note.user_id,
        event_start=note.event_start,
        subject=note.subject,
        info=note.info,
        contact_id=note.contact_id,
        pr_project_id=note.project_id,
        entry_id=note.entry_id,
        module_id=note.module_id
    )

    response = client.post(f'/note/{post_note.id}', post_note.dict())
    return parse_obj_as(Note, response)


def delete_note(note_id: int) -> DeleteResponse:
    client = BexioAPIClient()
    response = client.delete(f'/note/{note_id}')
    return parse_obj_as(DeleteResponse, response)


def search_note(query: NoteSearch) -> List[Note]:
    client = BexioAPIClient()
    response = client.post('/note/search', query.dict()['query'])
    return parse_obj_as(List[Note], response)
