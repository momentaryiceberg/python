"""
Tag Selector	        p	            Selects all <p> elements.
Class Selector	        .example	    Selects all elements with the class name “example”.
ID Selector	            #example	    Selects the element with the ID “example”.
Attribute Selector	    [type="text"]	Selects all elements with the attribute “type” and value “text”.
Descendant Selector	    div p	        Selects all <p> elements that are descendants of a <div> element.
Child Selector	        ul > li	        Selects all <li> elements that are direct children of a <ul> element.
Pseudo-Class Selector	a:hover	        Selects all <a> elements when the mouse is hovering over them."""

""" SELECTOLAX
from selectolax.parser import HTMLParser

tree = HTMLParser(html)
tree.css_first('h1#title').text()
tree.css_first('h1#title').attributes                    """

"""Komast að því hvernig best er að scrape-a javascript frontend síður, er það API endpoints?"""

import httpx
from selectolax.parser import HTMLParser

url = "https://www.visir.is/f/frettir-innlent"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

# Það sem maður fær til baka frá servernum er geymt í þessu variable
resp = httpx.get(url, headers=headers)

html = HTMLParser(resp.text)

# skilar fyrsta css selectornum, .text() skilar texta þess elements
print(html.css_first("title").text())

# hér er valið mengið sem inniheldur það sem maður vill scrape-a, til að svo filtera niður til þeirra atriða sem maður vill.
# .css skilar öllu sem matchar
parent = html.css("body > div.main-content > section > div.limit.padded > div")

greinar_row = html.css("div.row")

greinar = html.css("div.article-item article-item--split -news")

for grein in greinar:
    titill = html.css_first("h2").text()
    texti = html.css_first("p").text()
    timi = html.css_first("time.article-item__time").text()
    print(f"""
Titill: {titill}
Texti: {texti}
Tími: {timi}
""")


