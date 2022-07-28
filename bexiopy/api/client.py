import json

import requests

from bexiopy.api.settings import Settings


class BexioAPIException(Exception):
    def __init__(self, error):
        super(BexioAPIException, self).__init__(error)


class BexioAPIClient:
    BEXIO_BASE_URL = 'https://api.bexio.com/'
    BEXIO_API_DEFAULT_VERSION = '2.0'

    def __init__(self, api_version=None):
        settings: Settings = Settings()
        self.api_key = settings.bexio_api_key

        if not self.api_key:
            raise Exception('Missing api key for Bexio.')

        if not api_version:
            api_version = self.BEXIO_API_DEFAULT_VERSION

        self.BASE_URL = f'{self.BEXIO_BASE_URL}{api_version}'

        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def call(self, method, endpoint, **kwargs):
        data = None
        if 'data' in kwargs and kwargs['data'] is not None:
            data = json.dumps(kwargs['data'])

        response = getattr(requests, method)(f'{self.BASE_URL}{endpoint}', data=data, headers=self.headers)

        if response.status_code not in [200, 201, 204]:
            raise BexioAPIException(response.json())

        return response.json()

    def get(self, endpoint):
        return self.call('get', endpoint)

    def post(self, endpoint, payload=None):
        return self.call('post', endpoint, data=payload)

    def put(self, endpoint, payload=None):
        return self.call('put', endpoint, data=payload)

    def patch(self, endpoint, payload=None):
        return self.call('patch', endpoint, data=payload)

    def delete(self, endpoint, payload=None):
        return self.call('delete', endpoint, data=payload)
