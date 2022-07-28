from typing import List
from unittest.mock import patch

from bexiopy.other.countries import get_country, get_countries
from bexiopy.other.models import Country
from tests.other.factroeris import CountryFactory


@patch('bexiopy.api.client.requests.get')
def test_get_countries(mock_get):
    countries: List[Country] = CountryFactory.batch(5)

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = countries

    r_countries: List[Country] = get_countries()

    assert mock_get.called
    assert r_countries == countries


@patch('bexiopy.api.client.requests.get')
def test_get_country(mock_get):
    country: Country = CountryFactory.build()

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = country

    r_country: Country = get_country(1)

    assert mock_get.called
    assert r_country == country
