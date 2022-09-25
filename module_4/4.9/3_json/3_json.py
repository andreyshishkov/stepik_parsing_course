import json
from bs4 import BeautifulSoup
import requests


CATEGORY = 'mouse'


def get_soup(url: str) -> BeautifulSoup:
    """Prepare soup for current url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_urls(soup: BeautifulSoup) -> list[str]:
    """Create urls of all items of category"""
    page_urls = [x['href'] for x in soup.find('div', class_='pagen').find_all('a')]
    page_urls = [f"https://parsinger.ru/html/{page}" for page in page_urls]
    items_urls = []
    for page in page_urls:
        page_soup = get_soup(page)
        items = page_soup.find_all('div', class_='item')
        items = [x.find('a', class_='name_item')['href'] for x in items]
        items = [f"https://parsinger.ru/html/{x}" for x in items]
        items_urls.extend(items)
    return items_urls


def get_descr_of_item(soup: BeautifulSoup) -> dict[str]:
    headers = ['brand', 'model', 'type', 'gaming', 'light',
               'size', 'dpi', 'site of manufacturer'
               ]
    descr = soup.find('ul', id='description').find_all('li')
    descr = [prop.text.split(': ')[1] for prop in descr]
    return dict(zip(headers, descr))


def get_items(item_urls: list[str]) -> list[dict]:
    """Return necessary data about items"""
    items = []
    for url in item_urls:
        soup = get_soup(url)
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        description = get_descr_of_item(soup)
        item_dict = {
            'category': CATEGORY,
            'name': name,
            'article': article,
            'description': description,
            'in stock': in_stock,
            'price': price,
            'old_price': old_price,
            'link': url
        }
        items.append(item_dict)

    return items


if __name__ == '__main__':
    start_url = 'https://parsinger.ru/html/index3_page_1.html'
    start_soup = get_soup(start_url)
    urls_of_items = get_urls(start_soup)
    result = get_items(urls_of_items)
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
