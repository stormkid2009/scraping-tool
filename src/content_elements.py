from typing import List, Dict

def get_content_elements_from_user() -> List[Dict[str, str]]:
    content_elements = []

    while True:
        tag = input("Enter the tag (e.g., h1, p, img): ").strip()
        if not tag:
            print("Tag cannot be empty. Please enter a valid tag.")
            continue

        # Get class name and id
        class_name = input("Enter the class name (leave empty if not applicable): ").strip()
        element_id = input("Enter the id (leave empty if not applicable): ").strip()

        if not class_name and not element_id:
            print("Either class name or id must be provided. Please enter at least one.")
            continue

        # Construct the element dictionary
        element = {"tag": tag}
        if class_name:
            element["class"] = class_name
        if element_id:
            element["id"] = element_id

        content_elements.append(element)

        add_more = input("Add another element? (y/n): ").strip().lower()
        if add_more != 'y':
            break

    return content_elements
