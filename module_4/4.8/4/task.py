import requests
import csv
from bs4 import BeautifulSoup

# 1 ---------------------------------------------------
headers = 'Наименование, Артикул, Бренд, Модель, Наличие, Цена, Старая цена, Ссылка на карточку с товаром'.split(', ')
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(headers)
# 1----------------------------------------------------


# 2----------------------------------------------------
url = 'http://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(url)
start_soup = BeautifulSoup(start_response.text, 'lxml')

category_links = [x['href'] for x in start_soup.find('div', class_='nav_menu').find_all('a')]

all_values = []
for category in category_links:
    category_response = requests.get(f'http://parsinger.ru/html/{category}')
    category_soup = BeautifulSoup(category_response.text, 'lxml')

    pages = [x['href'] for x in category_soup.find('div', class_='pagen').find_all('a')]

    for page in pages:
        page_url = f'http://parsinger.ru/html/{page}'
        page_response = requests.get(page_url)
        page_soup = BeautifulSoup(page_response.text, 'lxml')

        items = [x['href'] for x in page_soup.find_all('a', class_='name_item')]

        for item in items:
            item_url = f'http://parsinger.ru/html/{item}'
            item_response = requests.get(item_url)
            item_response.encoding = 'utf-8'
            item_soup = BeautifulSoup(item_response.text, 'lxml')

            name = item_soup.find('p', id='p_header').text
            article = item_soup.find('p', class_='article').text.split()[1]

            brand_model = [x.text.split()[1] for x in item_soup.find('ul', id='description').find_all('li')[:2]]
            in_stock = item_soup.find('span', id='in_stock').text.split()[2]
            price = item_soup.find('span', id='price').text.split()[0]
            old_price = item_soup.find('span', id='old_price').text.split()[0]

            values = [name] + [article] + brand_model + [in_stock] + [price] + [old_price] + [item_url]
            all_values.append(values)
# 2---------------------------------------------------------------------------------------

# 3-------------------------------------------------------------------------------------
with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(all_values)
print('File is created')
# 3-------------------------------------------------------------------------------------
