# web_scraping_project/scraper.py

import requests
from bs4 import BeautifulSoup
from .input_handler import get_user_url  # Import the function from the module

def scrape():
    url = get_user_url()  # Get the URL from the user
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    print(soup.title.text)

if __name__ == "__main__":
    scrape()
