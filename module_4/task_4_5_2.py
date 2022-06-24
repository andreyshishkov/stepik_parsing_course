import requests
from bs4 import BeautifulSoup

url1 = 'http://parsinger.ru/html/index3_page_4.html'
response = requests.get(url=url1)
soup1 = BeautifulSoup(response.text, 'lxml')

pagen = [link['href'] for link in soup1.find('div', class_='pagen').find_all('a')]

all_sum = 0
for url in pagen:

    response = requests.get(url=f'http://parsinger.ru/html/{url}')
    soup = BeautifulSoup(response.text, 'lxml')
    items = [link['href'] for link in soup.find_all('a', class_='name_item')]

    for item in items:
        item_response = requests.get(url=f'http://parsinger.ru/html/{item}')
        item_soup = BeautifulSoup(item_response.text, 'lxml')
        obj = item_soup.find('p', class_='article')
        article = int(obj.text.split()[-1])
        all_sum += article

    articles = [int(num.split()[-1]) for num in soup.find_all('p', class_='article')]
    all_sum += sum(articles)

print(all_sum)
