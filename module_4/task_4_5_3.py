import requests
from bs4 import BeautifulSoup

start_url = 'http://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(url=start_url)
start_soup = BeautifulSoup(start_response.text, 'lxml')
categories = [link['href'] for link in start_soup.find('div', class_='nav_menu').find_all('a')]

summary = 0
for category in categories:
    start_cat_response = requests.get(url=f'http://parsinger.ru/html/{category}')
    cat_soup = BeautifulSoup(start_cat_response.text, 'lxml')
    pages = [link['href'] for link in cat_soup.find('div', class_='pagen').find_all('a')]

    for page in pages:
        page_response = requests.get(url=f'http://parsinger.ru/html/{page}')
        page_soup = BeautifulSoup(page_response.text, 'lxml')
        items = [link['href'] for link in page_soup.find_all('a', class_='name_item')]

        for item in items:
            item_response = requests.get(url=f'http://parsinger.ru/html/{item}')
            item_soup = BeautifulSoup(item_response.text, 'lxml')
            amount = int(item_soup.find('span', id='in_stock').text.split()[-1])
            price = int(item_soup.find('span', id='price').text.split()[0])
            summary += amount * price

print(summary)
