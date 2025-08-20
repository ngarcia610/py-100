import requests
from bs4 import BeautifulSoup

def get_text_from_element(url, tag, attrs=None):
    try:
        # Fetch HTML
        response = requests.get(url)
        response.raise_for_status()

        # Parse
        soup = BeautifulSoup(response.text, "html.parser")

        # Find elements matching tag + attributes
        elements = soup.find_all(tag, attrs=attrs)

        # Extract text
        texts = [el.get_text(strip=True) for el in elements]

        return texts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

# Example usage:
url = "https://www.lincolntech.edu/campus/levittown-pa/programs/automotive-technology/automotive-service-technology-diploma"
tag = "span"
attrs = {"property": "schema:name"}   # target <span property="schema:name">

texts = get_text_from_element(url, tag, attrs)

for i, text in enumerate(texts, 1):
    print(f"{i}. {text}")