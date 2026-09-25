from weather.clients.exceptions import CountryServiceException
import requests

from weather.clients.exceptions import (
    CountryServiceException,
    CountryNotFoundException
)
class CountryClient:

    def get_by_country_name(self, country_name):
        url = f'{self.base_url}/countries/v5/names.common/{country_name}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
        except requests.exceptions.Timeout as exc:
            raise CountryServiceException("Countries API timed out") from exc
        except requests.exceptions.ConnectionError as exc:
            raise CountryServiceException("Countries API unreachable") from exc

        if response.status_code == 404:
            raise CountryNotFoundException(f"No country found for '{country_name}'")
        if not response.ok:
            raise CountryServiceException(f"Countries API returned {response.status_code}")

        try:
            return response.json()
        except ValueError as exception:
            raise CountryServiceException("Countries API returned invalid JSON") from exception

    def __init__(self, base_url, api_key, timeout=5):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
