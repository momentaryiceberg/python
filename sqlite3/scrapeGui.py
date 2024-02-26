import httpx
from selectolax.parser import HTMLParser
import tkinter as tk
from tkinter import scrolledtext

def scrape_titill():
    url = "https://www.visir.is/"
    resp = httpx.get(url)
    html = HTMLParser(resp.text)

    titill = html.css_first("title").text()
    return titill

def scrape_text():
    pass

def scrape_glugg():
    glugg = tk.Toplevel(root)
    glugg.title(scrape_titill())

    text_widget = scrolledtext.ScrolledText(glugg, wrap="word")
    text_widget.pack(fill="both", expand=True)

    # Assuming the function scraped_text() returns the scraped text
    scraped_text = scrape_text()

    text_widget.insert("end", scraped_text)

root = tk.Tk() 

glugg_button = tk.Button(root, text="Sjá skrap", command=scrape_glugg).pack()


root.mainloop()