import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.orangepage.net/recipes/search/6')
soup = BeautifulSoup(res.text, 'html.parser')
text = soup.h2.string
print(text)
