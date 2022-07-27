from enum import Enum
from typing import List

from pydantic import BaseModel, validator


class SearchCriteria(str, Enum):
    equal = '='
    not_equal = '!='
    greater_than = '>'
    less_than = '<'
    greater_equal = '>='
    less_equal = '<='
    like = 'like'
    not_like = 'not_like'
    is_null = 'is_null'
    not_null = 'not_null'
    is_in = 'in'
    not_in = 'not_in'


class SearchQuery(BaseModel):
    field: str
    value: str
    criteria: SearchCriteria = SearchCriteria.like


class Search(BaseModel):
    query: List[SearchQuery]
    _allowed_search_fields: List[str] = []

    @validator('query')
    def search_field_is_allowed(cls, values):
        for value in values:
            assert value.field in cls._allowed_search_fields, f'Search field "{value.field}" not allowed!'
        return values


class DeleteResponse(BaseModel):
    success: bool


