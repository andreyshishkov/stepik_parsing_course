# this script outputs sum of prices of clocks from one site

import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
prices = [x.text for x in soup.find_all('p', class_='price')]
prices = [int(x.split()[0]) for x in prices]
print(sum(prices))
