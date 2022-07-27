from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.other.models import CompanyProfile


def get_company_profiles() -> List[CompanyProfile]:
    client = BexioAPIClient()
    response = client.get('/company_profile')
    return parse_obj_as(List[CompanyProfile], response)


def get_company_profile(profile_id: int) -> CompanyProfile:
    client = BexioAPIClient()
    response = client.get('/company_profile/{profile_id}')
    return parse_obj_as(CompanyProfile, response)
