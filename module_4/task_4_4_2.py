import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
old_price = soup.find('span', id='old_price').text
old_price = int(old_price.split()[0])

price = soup.find('span', id='price').text
price = int(price.split()[0])

result = (old_price - price) * 100 / old_price
print(f'{result:.1f}')