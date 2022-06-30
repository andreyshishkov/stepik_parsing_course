import requests
from bs4 import BeautifulSoup
import csv

# 1---------------------------------
string_of_columns = 'Наименование, Артикул, Бренд, Модель, ' \
          'Тип, Технология экрана, Материал корпуса, Материал браслета, ' \
          'Размер, Сайт производителя, Наличие, Цена, Старая цена, Ссылка на карточку с товаром'
columns = string_of_columns.split(', ')
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(columns)
# 1---------------------------------

# 2---------------------------------
url = 'http://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(url=url)
start_soup = BeautifulSoup(start_response.text, 'lxml')
pages = [x['href'] for x in start_soup.find('div', class_='pagen').find_all('a')]

descriptions = []
for page in pages:
    page_response = requests.get(url=f'http://parsinger.ru/html/{page}')
    page_soup = BeautifulSoup(page_response.text, 'lxml')
    items = [x['href'] for x in page_soup.find_all('a', class_='name_item')]

    for item in items:
        item_url = f'http://parsinger.ru/html/{item}'
        item_response = requests.get(url=item_url)
        item_response.encoding = 'utf-8'
        item_soup = BeautifulSoup(item_response.text, 'lxml').find('div', class_='description')

        name = item_soup.find('p', id='p_header').text
        article = item_soup.find('p', class_='article').text
        item_descr = [x.text.split(': ')[1] for x in item_soup.find_all('li')]
        stock = item_soup.find('span', id='in_stock').text.split(': ')[1]
        price = item_soup.find('span', id='price').text.split()[0]
        old_price = item_soup.find('span', id='old_price').text.split()[0]

        description = [name] + [article] + item_descr + [stock] + [price] + [old_price] + [item_url]
        descriptions.append(description)
# 2----------------------------------------

# 3---------------------------------------
with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(descriptions)
    print('File is created')
# 3----------------------------------
