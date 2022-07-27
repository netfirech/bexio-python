from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.other.models import PaymentType, PaymentTypeSearch


def get_payment_types() -> List[PaymentType]:
    client = BexioAPIClient()
    response = client.get('/payment_type')
    return parse_obj_as(List[PaymentType], response)


def search_payment_types(query: PaymentTypeSearch) -> List[PaymentType]:
    client = BexioAPIClient()
    response = client.post('/payment_type/search', query.dict()['query'])
    return parse_obj_as(List[PaymentType], response)
