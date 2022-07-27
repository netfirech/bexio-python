from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.other.models import Language, LanguageSearch


def get_languages() -> List[Language]:
    client = BexioAPIClient()
    response = client.get('/language')
    return parse_obj_as(List[Language], response)


def search_language(query: LanguageSearch) -> List[Language]:
    client = BexioAPIClient()
    response = client.post('/language/search', query.dict()['query'])
    return parse_obj_as(List[Language], response)
