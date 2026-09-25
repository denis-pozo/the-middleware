from unittest.mock import Mock, patch

from django.test import SimpleTestCase

from weather.clients.countries_client import CountryClient


class CountryClientGetByCountryNameTests(SimpleTestCase):

    def setUp(self):
        self.client = CountryClient(base_url="https://countries.example", api_key="secret", timeout=5)

    @patch("weather.clients.countries_client.get")
    def test_returns_json_body_on_success(self, mock_get):
        mock_get.return_value = Mock(status_code=200, ok=True, json=lambda: {"name": "Spain"})

        result = self.client.get_by_country_name("Spain")

        self.assertEqual(result, {"name": "Spain"})
        mock_get.assert_called_once_with(
            "https://countries.example/countries/v5/names.common/Spain",
            headers={"Authorization": "Bearer secret"},
            timeout=5,
        )
