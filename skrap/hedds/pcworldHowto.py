import httpx
from selectolax.parser import HTMLParser

url = "https://www.pcworld.com/security/how-to"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

pageTitle = html.css_first("title").text()

greinar = html.css("article.item")

greinar_texti = greinar.css_first("div.item-text")

for greinar_t in greinar_texti:
    print(greinar_t.text())


# a.btn.