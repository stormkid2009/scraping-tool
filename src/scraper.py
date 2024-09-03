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
    print(elements_list)
    # Dictionary to hold the data for CSV
    csv_data = {}

    # Iterate through the list of dictionaries
    for element in elements_list:
        tag = element['tag']
        class_name = element.get('class')
        element_id = element.get('id')
        
        # Find elements based on class name or id
        if class_name and element_id:
            found_elements = soup.find_all(tag, class_=class_name, id=element_id)
        elif class_name:
            found_elements = soup.find_all(tag, class_=class_name)
        elif element_id:
            found_elements = soup.find_all(tag, id=element_id)
        else:
            found_elements = []

        # Store the text content in the dictionary with a key based on class_name or id
        key = class_name if class_name else element_id
        csv_data[key] = [elem.get_text(strip=True) for elem in found_elements]

    # Write the data to a CSV file
    write_to_csv('output.csv', csv_data)
    #print (csv_data)

if __name__ == "__main__":
    scrape()
