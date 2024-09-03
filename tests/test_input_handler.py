import pytest
from unittest.mock import patch
from src.input_handler import get_user_url


@patch('builtins.input', return_value="http://example.com")

def test_get_user_url(mock_input):
    """
    Tests the get_user_url function to ensure it returns the correct URL.

    This test case uses the patch decorator to mock the built-in input function,
    returning a predefined URL. It then calls the get_user_url function and
    asserts that the returned URL matches the expected value.

    Parameters:
        None

    Returns:
        None
    """
    url = get_user_url()
    assert url == "http://example.com"
