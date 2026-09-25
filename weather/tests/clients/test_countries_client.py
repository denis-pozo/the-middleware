import requests
from weather.clients.exceptions import (
    CountryServiceException,
    CountryNotFoundException
)
from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from weather.clients.countries_client import CountryClient


class CountryClientGetByCountryNameTests(SimpleTestCase):

    def setUp(self):
        self.client = CountryClient(base_url="https://countries.example", api_key="secret", timeout=5)

    @patch("requests.get")
    def test_returns_json_body_on_success(self, mock_get):
        mock_get.return_value = Mock(status_code=200, ok=True, json=lambda: {"name": "Spain"})

        result = self.client.get_by_country_name("Spain")

        self.assertEqual(result, {"name": "Spain"})
        mock_get.assert_called_once_with(
            "https://countries.example/countries/v5/names.common/Spain",
            headers={"Authorization": "Bearer secret"},
            timeout=5,
        )

    @patch("requests.get")
    def test_return_country_not_found_error_on_404_response(self, mock_get):
        mock_get.return_value = Mock(status_code=404)

        with self.assertRaises(CountryNotFoundException):
          self.client.get_by_country_name("Narnia")

    @patch("requests.get")
    def test_return_country_response_not_ok(self, mock_get):
        mock_get.return_value = Mock(ok=False)

        with self.assertRaises(CountryServiceException):
            self.client.get_by_country_name("Spain")

    @patch("requests.get")
    def test_client_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout()

        with self.assertRaises(CountryServiceException):
            self.client.get_by_country_name("Spain")

    @patch("requests.get")
    def test_client_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()

        with self.assertRaises(CountryServiceException):
            self.client.get_by_country_name("Spain")
    


        