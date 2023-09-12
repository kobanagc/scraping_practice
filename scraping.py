import requests
from bs4 import BeautifulSoup
from selenium import webdriver

res = requests.get('https://www.orangepage.net/recipes/search/6')
soup = BeautifulSoup(res.text, 'html.parser')

# 最初のh2タグを表示
text = soup.h2.string
print(text)

# h2タグの中身を表示
h2_tags = soup.find_all('h2')
h2_strings = [tag.string for tag in h2_tags]
print(h2_strings)

# 最初のh3タグを表示
text = soup.h3.string
print(text)

# h2タグの中身を表示
h3_tags = soup.find_all('h3')
h3_strings = [tag.string for tag in h3_tags]
print(h3_strings)

# selenium

# ブラウザを立ち上げないようにする
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)
# 待機時間を設定
driver.implicitly_wait(10)
driver.get('https://www.library.chiyoda.tokyo.jp/')
schedule_el = driver.find_elements_by_class_name('schedule')
print([s.text for s in schedule_el])

schedule_el2 = driver.find_elements_by_xpath('//li[@id="chiyoda-today-status"]/div/div/span')
print([s.text for s in schedule_el2])