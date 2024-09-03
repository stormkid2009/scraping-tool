from unittest.mock import patch, MagicMock
from src.scraper import scrape

@patch('src.scraper.write_to_csv')
@patch('src.scraper.get_content_elements_from_user')
@patch('src.scraper.parse_content')
@patch('src.scraper.fetch_page')
@patch('src.scraper.get_user_url')
def test_scrape(mock_get_user_url, mock_fetch_page, mock_parse_content, mock_get_content_elements_from_user, mock_write_to_csv):
    # Set up mocks
    mock_get_user_url.return_value = 'http://example.com'

    mock_response = MagicMock()
    mock_response.content = b'<html><head><title>Test Page</title></head><body><h1 class="header">Header 1</h1><p id="paragraph">Paragraph 1</p></body></html>'
    mock_fetch_page.return_value = mock_response

    mock_soup = MagicMock()
    mock_soup.title.text = 'Test Page'
    mock_soup.find_all.side_effect = lambda tag, **kwargs: [MagicMock(get_text=lambda strip=True: f'{tag} content')]
    mock_parse_content.return_value = mock_soup

    mock_get_content_elements_from_user.return_value = [
        {"tag": "h1", "class": "header"},
        {"tag": "p", "id": "paragraph"},
    ]

    # Call the scrape function
    scrape()
    #print("write_to_csv was called with:", mock_write_to_csv.call_args)

    # Assertions
    mock_get_user_url.assert_called_once()
    mock_fetch_page.assert_called_once_with('http://example.com')
    mock_parse_content.assert_called_once_with(mock_response.content)
    mock_get_content_elements_from_user.assert_called_once()

    # Check if the find_all was called correctly
    assert mock_soup.find_all.call_count == 2
    mock_soup.find_all.assert_any_call('h1', class_='header')
    mock_soup.find_all.assert_any_call('p', id='paragraph')

    # Check if write_to_csv was called with the expected data
    expected_csv_data = {
        'header': ['h1 content'],
        'paragraph': ['p content'],
    }
    #print("expected_csv_data:", expected_csv_data)
    
    #print("Checking mock_write_to_csv call")
    mock_write_to_csv.assert_called_once_with('output.csv', expected_csv_data)
    #print("mock_write_to_csv call passed")
    
