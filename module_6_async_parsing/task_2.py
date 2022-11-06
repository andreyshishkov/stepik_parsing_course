import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from aiohttp_retry import ExponentialRetry, RetryClient
import shutil


domain = 'https://parsinger.ru/asyncio/create_soup/1/'
values = []


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


async def get_data(session, url):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(
        retry_options=retry_options,
        client_session=session
    )
    async with retry_client.get(url) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            curr_val = soup.find('p', class_='text').text
            curr_val = int(curr_val)

            values.append(curr_val)


async def main():
    start_url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
    soup = get_soup(start_url)
    links = soup.find_all('a', class_='lnk_img')
    links = [domain + x['href'] for x in links]

    async with aiohttp.ClientSession() as session:

        tasks = []
        for link in links:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)

        await asyncio.gather(*tasks)
        print(sum(values))


if __name__ == '__main__':
    asyncio.run(main())


