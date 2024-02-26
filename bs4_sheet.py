# Importing necessary libraries
from bs4 import BeautifulSoup
import requests

# Function to create a BeautifulSoup object from a URL
def create_soup_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Function to create a BeautifulSoup object from an HTML string
def create_soup_from_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    return soup

# Example URL to work with
url = 'https://example.com'

# Creating a BeautifulSoup object from a URL
soup = create_soup_from_url(url)

# Extracting the title of the page
title = soup.title.text
print(f'Title: {title}')

# Finding all links in the page
links = soup.find_all('a')
for link in links:
    print(f'Link: {link["href"]}')

# Finding a specific element by its ID
element_with_id = soup.find(id='some_id')
print(f'Element with ID: {element_with_id}')

# Finding elements with a specific class
elements_with_class = soup.find_all(class_='some_class')
for element in elements_with_class:
    print(f'Element with Class: {element}')

# Extracting text content from an element
some_element = soup.find('div', class_='some_class')
text_content = some_element.get_text(strip=True)
print(f'Text Content: {text_content}')

# Navigating through the HTML structure
parent_element = some_element.parent
print(f'Parent Element: {parent_element}')

# Finding next and previous siblings
next_sibling = some_element.find_next_sibling()
prev_sibling = some_element.find_previous_sibling()
print(f'Next Sibling: {next_sibling}')
print(f'Previous Sibling: {prev_sibling}')

# Modifying HTML content
some_element.string = 'New Text Content'
print(f'Modified Text Content: {some_element}')

# Extracting attribute values
some_attribute_value = some_element['some_attribute']
print(f'Some Attribute Value: {some_attribute_value}')
