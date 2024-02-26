import requests
from selectolax.parser import HTMLParser
from collections import defaultdict

def get_css_selectors_sorted(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using selectolax
        html = response.text
        tree = HTMLParser(html)
        
        # Dictionary to store selectors and their occurrences
        selector_counts = defaultdict(int)
        
        # Extract all elements with a 'class' or 'id' attribute
        for element in tree.css("*[class], *[id]"):
            # Extract the class attribute
            classes = element.attributes.get("class", "").split()
            # Extract the id attribute
            ids = element.attributes.get("id", "").split()
            
            # Add each class and id to the dictionary with their occurrences
            for css_class in classes:
                selector_counts[f".{css_class}"] += 1
            for css_id in ids:
                selector_counts[f"#{css_id}"] += 1
                
        # Sort selectors by occurrences
        sorted_selectors = sorted(selector_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Return the sorted selectors
        return sorted_selectors
    else:
        # If request failed, return None
        print(f"Failed to fetch URL: {url}")
        return None

# Example usage:
url = "https://www.visir.is/f/frettir-innlent"
sorted_selectors = get_css_selectors_sorted(url)
if sorted_selectors:
    for selector, count in sorted_selectors:
        print(f"{selector}: {count} occurrences")
