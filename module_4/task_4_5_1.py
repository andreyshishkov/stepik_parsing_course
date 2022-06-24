import requests
from bs4 import BeautifulSoup

urls = []
for i in range(1, 5):
    urls.append(f'http://parsinger.ru/html/index3_page_{i}.html')

all_means = []
for url in urls:
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    means = soup.find_all('a', class_='name_item')
    means = [obj.text for obj in means]
    all_means.append(means)
print(all_means)