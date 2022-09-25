import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_soup(url: str):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


start_url = "https://parsinger.ru/html/index1_page_1.html"
start_soup = get_soup(start_url)

category_links = start_soup.find('div', class_="nav_menu").find_all('a')
category_links = [category['href'] for category in category_links]
category_links = [f"https://parsinger.ru/html/{category}"
                  for category in category_links
                  ]

properties = [
    ['name', 'brand', 'type', 'material of corpus', 'technology of screen', 'price'],
    ['name', 'brand', 'diagonal', 'material', 'size', 'price'],
    ['name', 'brand', 'type', 'connect', 'game', 'price'],
    ['name', 'brand', 'form factor', 'size', 'volume of buffer', 'price'],
    ['name', 'brand', 'connect', 'color', 'type of headphones', 'price']
]


all_items = []
# scrolling of categories
for index, category in enumerate(tqdm(category_links)):
    category_soup = get_soup(category)

    cat_properties = properties[index]
    page_links = [f"https://parsinger.ru/html/{page['href']}"
                  for page in category_soup.find('div', class_='pagen').find_all('a')
                  ]

    # make scrolling of pages of category
    for page in page_links:
        page_soup = get_soup(page)
        item_cards = page_soup.find_all('div', class_='item')
        for item_card in item_cards:
            name = item_card.find('a', class_='name_item').text

            # take properties of item
            raw_descr = [prop.text
                         for prop in item_card.find('div', class_='description').find_all('li')
                         ]
            descr = [prop.split(':')[1] for prop in raw_descr]
            descr = [prop.strip() for prop in descr]

            price = item_card.find('p', class_='price').text

            item = [name] + descr + [price]
            all_items.append(dict(
                zip(cat_properties, item)
            )
            )

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(all_items, file, indent=4, ensure_ascii=False)
