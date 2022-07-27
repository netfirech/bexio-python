from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.other.models import UserPermission


def get_permissions() -> UserPermission:
    client = BexioAPIClient(api_version='3.0')
    response = client.get('/permissions')
    return parse_obj_as(UserPermission, response)
