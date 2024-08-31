# src/content_elements.py

from typing import List, Dict

def get_content_elements_from_user() -> List[Dict[str, str]]:
    content_elements = []

    while True:
        tag = input("Enter the tag (e.g., h1, p, img): ").strip()
        if not tag:
            print("Tag cannot be empty. Please enter a valid tag.")
            continue

        class_name = input("Enter the class name: ").strip()
        while not class_name:  # Loop until a valid class name is entered
            print("Class name cannot be empty. Please enter a valid class name.")
            class_name = input("Enter the class name: ").strip()

        content_elements.append({"tag": tag, "class": class_name})

        add_more = input("Add another element? (y/n): ").strip().lower()
        if add_more != 'y':
            break

    return content_elements