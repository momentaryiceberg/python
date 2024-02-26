from bs4 import BeautifulSoup
import requests

url = "https://vb.is/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(_class="article-block_title")
#parent = prices[0].parent
#strong = parent.find("strong")

print(prices)
