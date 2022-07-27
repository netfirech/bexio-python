from typing import List

from pydantic import parse_obj_as

from bexiopy.api.client import BexioAPIClient
from bexiopy.api.models import DeleteResponse
from bexiopy.other.models import Country, CountrySearch, CountryPost


def get_countries() -> List[Country]:
    client = BexioAPIClient()
    response = client.get('/country')
    return parse_obj_as(List[Country], response)


def get_country(country_id: int) -> Country:
    client = BexioAPIClient()
    response = client.get(f'/country/{country_id}')
    return parse_obj_as(Country, response)


def create_country(country: CountryPost) -> Country:
    client = BexioAPIClient()
    response = client.post('/country', country.dict())
    return parse_obj_as(Country, response)


def edit_country(country: Country) -> Country:
    client = BexioAPIClient()

    # Mapping between the Country and CountryPost schema.
    # This needs to be done until Bexio fixed the inconsistency in their /country endpoint
    country: CountryPost = CountryPost(
        id=country.id,
        name=country.name,
        name_short=country.name_short,
        iso3166_alpha2=country.iso_3166_alpha2
    )

    response = client.post(f'/country/{country.id}', country.dict())
    return parse_obj_as(Country, response)


def delete_country(country_id: int) -> DeleteResponse:
    client = BexioAPIClient()
    response = client.delete(f'/country/{country_id}')
    return parse_obj_as(DeleteResponse, response)


def search_country(query: CountrySearch) -> List[Country]:
    client = BexioAPIClient()
    response = client.post('/country/search', query.dict()['query'])
    return parse_obj_as(List[Country], response)
