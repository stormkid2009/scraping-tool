import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.MissingSchema:
        raise  # Re-raise MissingSchema
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
