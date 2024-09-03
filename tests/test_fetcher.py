import pytest
import requests
from requests.exceptions import Timeout, HTTPError
from src.fetcher import fetch_page


def test_fetch_page_success(requests_mock):
    url = "https://example.com"
    mock_response = requests_mock.get(url, text="mocked response")

    response = fetch_page(url)

    assert response is not None
    assert response.status_code == 200
    assert response.text == "mocked response"


def test_fetch_page_timeout(requests_mock):
    url = "https://example.com"
    requests_mock.get(url, exc=Timeout)

    response = fetch_page(url)

    assert response is None


def test_fetch_page_http_error(requests_mock):
    url = "https://example.com"
    requests_mock.get(url, status_code=404)

    response = fetch_page(url)

    assert response is None


def test_fetch_page_invalid_url(requests_mock):
    url = "invalid-url"
    with pytest.raises(requests.exceptions.MissingSchema):
        fetch_page(url)
