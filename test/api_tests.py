import pytest
from unittest.mock import Mock
import requests
from back_weather_api import get_coords, get_weather

# Mocking requests.get for testing purposes
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def test_get_coords():
    # Mocking the response for successful API call
    mock_response = MockResponse([{"lat": 45.7578137, "lon": 4.8320114}], 200)
    requests.get = Mock(return_value=mock_response)

    city = "Lyon"
    lat, lon = get_coords(city)

    assert lat == 45.7578137
    assert lon == 4.8320114

def test_get_weather():
    # Mocking the response for successful API call
    mock_response = MockResponse({
        "weather": [{"description": "Clear sky"}],
        "main": {},
        "clouds": {"all": 0}
    }, 200)
    requests.get = Mock(return_value=mock_response)

    lat, lon = 45.7578137, 4.8320114
    weather, main, cloud = get_weather(lat, lon)

    assert weather == "Clear sky"
    assert main == {}
    assert cloud == 0

def test_get_coords_error():
    # Mocking the response for an error status code
    mock_response = MockResponse({}, 404)
    requests.get = Mock(return_value=mock_response)

    city = "Lyon"
    lat, lon = get_coords(city)

    assert lat is None
    assert lon is None

def test_get_weather_error():
    # Mocking the response for an error status code
    mock_response = MockResponse({}, 500)
    requests.get = Mock(return_value=mock_response)

    lat, lon = 45.7578137, 4.8320114
    result = get_weather(lat, lon)

    assert result is None
