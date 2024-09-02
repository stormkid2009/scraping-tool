# src/scraper.py

from .input_handler import get_user_url
from .fetcher import fetch_page
from .parser import parse_content
from .content_elements import get_content_elements_from_user
from .csv_writer import write_to_csv

def scrape():
    url = get_user_url()  # Get the URL from the user
    response = fetch_page(url)
    soup = parse_content(response.content)

    print(soup.title.text)
    
    # Get elements list from user input
    elements_list = get_content_elements_from_user()

    # Dictionary to hold the data for CSV
    csv_data = {}

    # Iterate through the list of dictionaries
    for element in elements_list:
        tag = element['tag']
        class_name = element['class']
        
        # Find all elements matching the tag and class name
        found_elements = soup.find_all(tag, class_=class_name)
        #found_elements = soup.find_all(tag, id=class_name)
        # Store the text content in the dictionary with class_name as the key
        csv_data[class_name] = [elem.get_text(strip=True) for elem in found_elements]

    # Write the data to a CSV file
    write_to_csv('output.csv', csv_data)

if __name__ == "__main__":
    scrape()
