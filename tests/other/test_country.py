from typing import List

from bexiopy.other.countries import get_countries, get_country, create_country, delete_country
from bexiopy.other.models import Country, CountryPost


def test_get_countries():
    countries: List[Country] = get_countries()
    assert len(countries) is not 0


def test_get_country():
    countries: List[Country] = get_countries()
    country_id: int = countries[0].id

    country: Country = get_country(country_id)

    assert country.id == country_id


def test_create_country():
    country: Country = create_country(
        CountryPost(
            name='TestCountry',
            name_short='TC',
            iso3166_alpha2='CH'
        )
    )
    delete_country(country.id)
