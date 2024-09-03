import pytest
from unittest.mock import patch
from src.content_elements import get_content_elements_from_user

@pytest.mark.parametrize("side_effect, expected_output", [
    (['h1', 'header', '', 'y', 'p', '', 'para-id', 'n'], [
        {"tag": "h1", "class": "header"},
        {"tag": "p", "id": "para-id"},
    ]),
    (['h1', '', '', 'h1', 'header', '', 'n'], [
        {"tag": "h1", "class": "header"},
    ]),
    (['', 'h1', 'header', 'header-id', 'n'], [
        {"tag": "h1", "class": "header", "id": "header-id"},
    ]),
    (['div', '', 'div-id', 'n'], [
        {"tag": "div", "id": "div-id"},
    ]),
    (['span', 'highlight', 'highlight-id', 'n'], [
        {"tag": "span", "class": "highlight", "id": "highlight-id"},
    ]),
])
@patch('builtins.input')
def test_get_content_elements_from_user(mock_input, side_effect, expected_output):
    mock_input.side_effect = side_effect
    result = get_content_elements_from_user()
    assert result == expected_output
