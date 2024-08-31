# tests/test_content_elements.py

import unittest
from unittest.mock import patch
from src.content_elements import get_content_elements_from_user

class TestGetContentElementsFromUser(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[
        'h1', 'header',  # First element: valid tag and class name
        'y',  # Continue adding elements
        'p', 'paragraph',  # Second element: valid tag and class name
        'n'  # Stop adding elements
    ])
    def test_get_content_elements_from_user(self, mock_input):
        expected_output = [
            {"tag": "h1", "class": "header"},
            {"tag": "p", "class": "paragraph"},
        ]
        result = get_content_elements_from_user()
        self.assertEqual(result, expected_output)


    @patch('builtins.input', side_effect=[
        'h1', 'header',  # First element: valid tag and class name
        'y',  # Continue adding elements
        'p',          # First tag
        '',           # Empty class name (re-prompt needed)
        'paragraph',  # Valid class name
        'n'           # No more elements
    ])
    def test_empty_class_name(self, mock_input):
        expected_output = [
            {"tag": "h1", "class": "header"},
            {"tag": "p", "class": "paragraph"},
        ]
        result = get_content_elements_from_user()
        self.assertEqual(result, expected_output)

        
    @patch('builtins.input', side_effect=[
        '', 'h1', 'header',  # First element: empty tag, then valid tag and class name
        'n'  # Stop adding elements
    ])
    def test_empty_tag(self, mock_input):
        expected_output = [
            {"tag": "h1", "class": "header"},
        ]
        result = get_content_elements_from_user()
        self.assertEqual(result, expected_output)

    



if __name__ == '__main__':
    unittest.main()
