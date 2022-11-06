import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


domain = 'https://parsinger.ru/html/'
values = []


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def get_cat_links(soup: BeautifulSoup) -> list[str]:
    links = soup.find('div', class_='nav_menu').find_all('a')
    links = [domain + link['href'] for link in links]
    return links


def get_page_links(cat_links: list[str]) -> list[str]:
    pages = []
    for cat_link in cat_links:
        soup = get_soup(cat_link)
        curr_pages = soup.find('div', class_='pagen').find_all('a')
        curr_pages = [domain + page['href'] for page in curr_pages]
        pages.extend(curr_pages)
    return pages


async def get_data(session, link):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(
        raise_for_status=False,
        retry_options=retry_options,
        client_session=session,
        start_timeout=0.5
    )
    value = 0

    async with retry_client.get(link) as response:
        if response.ok:
            resp = await response.text(encoding='utf-8')
            soup = BeautifulSoup(resp, 'lxml')
            item_cards = [x['href'] for x in soup.find_all('a', class_='name_item')]
            for item_link in item_cards:
                item_url = domain + item_link
                async with session.get(url=item_url) as item_response:
                    item_resp = await item_response.text(encoding='utf-8')
                    item_soup = BeautifulSoup(item_resp, 'lxml')

                    amount = item_soup.find('span', id='in_stock').text.split(': ')[1]
                    amount = int(amount)

                    price = item_soup.find('span', id='price').text.split()[0]
                    price = int(price)

                    old_price = item_soup.find('span', id='old_price').text.split()[0]
                    old_price = int(old_price)

                    value += (old_price - price) * amount
    values.append(value)


async def main():
    ua = UserAgent()
    fake_ua = {'user=agent': ua.random}

    async with aiohttp.ClientSession(headers=fake_ua) as session:
        start_url = 'https://parsinger.ru/html/index1_page_1.html'
        start_soup = get_soup(start_url)
        cat_links = get_cat_links(start_soup)
        page_links = get_page_links(cat_links)

        tasks = []
        for link in page_links:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)
        print(sum(values))


if __name__ == '__main__':
    asyncio.run(main())
        
