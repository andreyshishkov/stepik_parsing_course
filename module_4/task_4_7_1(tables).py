# task1
'''
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
arr_of_values = [float(x.text) for x in soup.find_all('td')]
unique = list(set(arr_of_values))
print(sum(unique))
'''

# task 2
'''
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

rows = soup.find_all('tr')
first_values = [x.find('td') for x in rows]
first_values = [float(x.text) for x in first_values if x is not None]
print(sum(first_values))
'''

# task 3
'''
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/3/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

values = soup.find_all('td')
values = [x.find('b') for x in values]
values = [float(x.text) for x in values if x is not None]
print(sum(values))
'''

# task 4
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/4/index.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

values = [float(x.text) for x in soup.find_all('td', class_='green')]
print(sum(values))