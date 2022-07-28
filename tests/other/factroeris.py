from typing import Any

from pydantic_factories import ModelFactory

from bexiopy.other.models import Country


class CountryFactory(ModelFactory[Any]):
    __model__ = Country
