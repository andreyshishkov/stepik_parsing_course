import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

# 1-------------------------------------------------
start_url = 'http://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(start_url)
start_soup = BeautifulSoup(start_response.text, 'lxml')
item_hrefs = [x['href'] for x in start_soup.find_all('a', class_='name_item')] # собираю страницы часов
# 1-------------------------------------------------

# 2------------------------------------------------
json_items = []
for item in tqdm(item_hrefs):

    item = {}
    item_url = f'http://parsinger.ru/html/{item}'
    item_response = requests.get(item_url)
    item_response.encoding = 'utf-8'
    item_soup = BeautifulSoup(item_response.text, 'lxml')

    name = item_soup.find('p', id='p_header').text
    price = item-item_soup.find('span', id='price').text.split()[0]
    item['name'] = name
    item['price'] = price

    fields = [x['id'] for x in item_soup.find('ul', id='description').find_all('li')]
    description = item_soup.find('ul', id='description')
    for field in fields:
        value = description.find('li', id=field).text.split()[1]
        item[field] = value

    json_items.append(item)
# 2---------------------------------------------------

# 3---------------------------------------------------
with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(json_items, file, ensure_ascii=False, indent=4)
# 3----------------------------------------------------
