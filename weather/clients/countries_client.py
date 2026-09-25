from requests import get, exceptions
from weather.clients.exceptions import CountryServiceError, CountryNotFoundError


class CountryClient:

    def get_by_country_name(self, country_name):
        url = f'{self.base_url}/countries/v5/names.common/{country_name}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = get(url, headers=headers, timeout=self.timeout)
        except exceptions.Timeout as e:
            raise CountryServiceError("Countries API timed out") from e
        except exceptions.ConnectionError as e:
            raise CountryServiceError("Countries API unreachable") from e

        if response.status_code == 404:
            raise CountryNotFoundError(f"No country found for '{country_name}'")
        if not response.ok:
            raise CountryServiceError(f"Countries API returned {response.status_code}")

        try:
            print(response.json())
            return response.json()
        except ValueError as exception:
            raise CountryServiceError("Countries API returned invalid JSON") from exception

    def __init__(self, base_url, api_key, timeout=5):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
