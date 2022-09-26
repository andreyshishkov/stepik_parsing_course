from bs4 import BeautifulSoup
import json
import requests

path = 'https://parsinger.ru/html/'


def get_soup(url: str) -> BeautifulSoup:
    """Return soup for current url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def get_cats_and_urls(head_url: str) -> list[tuple[str]]:
    """Return list of urls and categories for items"""
    cat_urls = []
    soup = get_soup(head_url)
    cat_soups = soup.find('div', class_='nav_menu').find_all('a')
    for cat_soup in cat_soups:
        category = cat_soup.find('div')['id']
        cat_url = path + cat_soup['href']  # create url for start page of category
        urls_of_cat = get_urls_of_cat(cat_url)
        urls_of_cat = [(category, url) for url in urls_of_cat]
        cat_urls.extend(urls_of_cat)
    return cat_urls


def get_urls_of_cat(category_url):
    soup = get_soup(category_url)
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
    """Return properties of item"""
    description = {}
    properties = soup.find('ul', id='description').find_all('li')
    for prop in properties:
        key = prop['id']
        value = prop.text.split(': ')[1]
        description[key] = value
    return description


def get_items(item_urls: list[tuple[str]]) -> list[dict]:
    """Return necessary data about items"""
    items = []
    for category, url in item_urls:
        soup = get_soup(url)
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        description = get_descr_of_item(soup)
        item_dict = {
            'category': category,
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
    cat_and_urls = get_cats_and_urls(start_url)
    item_cards = get_items(cat_and_urls)
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(item_cards, file, indent=4, ensure_ascii=False)
        print('File is created')
