import requests
import csv
from bs4 import BeautifulSoup

# 1------------------
with open('result_2.csv', 'w', encoding='utf-8-sig', newline='') as file:
    pass
# 1---------------------

# 2--------------------
url = 'http://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(url=url)
start_response.encoding = 'utf-8'
start_soup = BeautifulSoup(start_response.text, 'lxml')
categories = [x['href'] for x in start_soup.find('div', class_='nav_menu').find_all('a')]
# 2---------------------

# 3-------------------
result = []
for category in categories:
    category_response = requests.get(url=f'http://parsinger.ru/html/{category}')
    category_response.encoding = 'utf-8'
    category_soup = BeautifulSoup(category_response.text, 'lxml')
    pages_per_category = [x['href'] for x in category_soup.find('div', class_='pagen').find_all('a')]

    category_names, category_prices, category_descriptions = [], [], []
    for page in pages_per_category:
        page_response = requests.get(url=f'http://parsinger.ru/html/{page}')
        page_response.encoding = 'utf-8'
        page_soup = BeautifulSoup(page_response.text, 'lxml')

        page_names = [x.text.strip() for x in page_soup.find_all('a', class_='name_item')]
        page_prices = [x.text.strip() for x in page_soup.find_all('p', class_='price')]

        items = page_soup.find_all('div', class_='description')
        page_descriptions = []
        for item in items:
            decscript = [x.text.split(':')[1].strip().replace('"', '') for x in item.find_all('li')]
            page_descriptions.append(decscript)

        category_names.extend(page_names)
        category_prices.extend(page_prices)
        category_descriptions.extend(page_descriptions)

    category_result = []
    for name, description, price in zip(category_names, category_descriptions, category_prices):
        temp_arr = [name] + description + [price]
        category_result.append(temp_arr)
    result.extend(category_result)
# 3-------------------------

# 4----------------------
with open('result_2.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for row in result:
        writer.writerow(row)
print('File is created')
# 4-----------------------


