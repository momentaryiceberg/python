import httpx
from selectolax.parser import HTMLParser

url = "https://kisildalur.is/category/30"

resp = httpx.get(url)

html = HTMLParser(resp.text)

river = html.css("div.products ng-star-inserted")

vara = html.css("div.container")


for v in vara:
    print(v.text())