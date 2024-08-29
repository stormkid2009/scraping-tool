
# src/scraper.py

from .input_handler import get_user_url  # Import the function from the module
from .fetcher import fetch_page
from .parser import parse_content

# I want to make it reusable, so I will reuse the main script for the scraper
# the input handler should get more info from the user where we can use to scrape the site
# we shall make another function to write info inside csv file

def scrape():
    url = get_user_url()  # Get the URL from the user
    response = fetch_page(url)
    soup = parse_content(response.content)

    print(soup.title.text)

if __name__ == "__main__":
    scrape()
