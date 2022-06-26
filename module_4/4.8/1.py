import requests
import csv
from bs4 import BeautifulSoup

# 1 -------------------------
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Бренд', 'Форм-фактор',
                     'Ёмкость', 'Объём буф. памяти', 'Цена'])
# 1---------------------

# 2----------------------
url = 'http://parsinger.ru/html/index4_page_1.html'
start_response = requests.get(url=url)
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, 'lxml')
# 2----------------------

# 3---------------------
pages = [x['href'] for x in start_soup.find('div', class_='pagen').find_all('a')]

names, descriptions, prices = [], [], []
for page in pages:
    page_response = requests.get(url=f'http://parsinger.ru/html/{page}')
    page_response.encoding = 'utf-8'
    page_soup = BeautifulSoup(page_response.text, 'lxml')
    page_names = [x.text.strip() for x in page_soup.find_all('a', class_='name_item')]
    page_prices = [x.text.strip() for x in page_soup.find_all('p', class_='price')]
    items = page_soup.find_all('div', class_='description')
    page_descriptions = []
    for descript in items:
        item = [x.text.split(':')[1].strip().replace('"', '') for x in descript.find_all('li')]
        page_descriptions.append(item)
    names.extend(page_names)
    descriptions.extend(page_descriptions)
    prices.extend(page_prices)
# 3----------------------

# 4----------------
result = []
for name, description, price in zip(names, descriptions, prices):
    arr = [name] + description + [price]
    result.append(arr)
# 4-----------------

# 5-----------------
with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in result:
        writer.writerow(row)
    print('File is created')
# 5----------------
