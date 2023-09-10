import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.orangepage.net/recipes/search/6')
soup = BeautifulSoup(res.text, 'html.parser')

# 最初のh2タグを表示
text = soup.h2.string
print(text)

# h2タグの中身を表示
h2_tags = soup.find_all('h2')
h2_strings = [tag.string for tag in h2_tags]
print(h2_strings)