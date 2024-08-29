import requests


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for better control
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  # Provide some error feedback
        return None
