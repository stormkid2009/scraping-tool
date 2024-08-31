# src/content_elements.py

from typing import List, Dict

def get_content_elements_from_user() -> List[Dict[str, str]]:
    """Get content elements from user input."""
    content_elements = []

    while True:
        tag = input("Enter the tag (e.g., h1, p, img): ").strip()
        if not tag:
            print("Tag cannot be empty. Please enter a valid tag.")
            continue

        class_name = input("Enter the class name: ").strip()
        if not class_name:
            print("Class name cannot be empty. Please enter a valid class name.")
            continue

        content_elements.append({"tag": tag, "class": class_name})

        add_more = input("Add another element? (y/n): ").strip().lower()
        print(f"Add another element input: {add_more}")  # Debug print
        if add_more != 'y':
            break

    return content_elements
