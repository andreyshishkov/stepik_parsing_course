# dowload zip-arxiv
import requests

url = 'http://parsinger.ru/downloads/cooking_soup/index.zip'
response = requests.get(url=url)
with open('file.zip', 'wb') as file:
    file.write(response.content)


# extract data from zip
import zipfile

with zipfile.ZipFile('file.zip') as obj:
    obj.extractall()


# open it using bs4
from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'lxml')
    print(soup)
