from bs4 import BeautifulSoup

def parse_content(content):
    if not content:
        return None  # Handle empty or None content
    return BeautifulSoup(content, 'lxml')
