from bs4 import BeautifulSoup
import requests

def get_tags_and_attributes(url):
    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        html_content = response.text

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all tags in the HTML
        all_tags = soup.find_all(True)

        # Print tags and their attributes
        for tag in all_tags:
            tag_name = tag.name
            attributes = tag.attrs
            print(f'Tag: {tag_name}, Attributes: {attributes}')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")

# Example URL to test the script
# url_to_scrape = 'https://example.com'
url_to_scrape = input("Hvað er url-ið? : ")
get_tags_and_attributes(url_to_scrape)
