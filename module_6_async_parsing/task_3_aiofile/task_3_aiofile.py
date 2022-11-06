import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup
import requests
import asyncio
import aiofiles
import os


domain = 'https://parsinger.ru/asyncio/aiofile/2/'
unique_images = set()
image_number = 0


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


def get_hrefs(url: str) -> list[str]:
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    links_ = [x['href'] for x in soup.find_all('a', class_='lnk_img')]
    links_ = [domain + link for link in links_]

    return links_


async def get_image(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}.jpg', mode='wb') as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await file.write(x)


async def get_images_from_link(session, url):
    retry_options = ExponentialRetry(attempts=5)
    retry_client = RetryClient(
        raise_for_status=False,
        retry_options=retry_options,
        client_session=session,
        start_timeout=0.5
    )
    async with retry_client.get(url) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')

            img_links = [x['src'] for x in soup.find_all('img', class_='picture')]
            tasks = []
            for link in img_links:
                link_name = hash(link)
                if link_name not in unique_images:
                    task = asyncio.create_task(get_image(session, link, link_name))
                    tasks.append(task)
                    unique_images.add(link_name)
            await asyncio.gather(*tasks)


async def main(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in urls:
            task = asyncio.create_task(get_images_from_link(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
    links = get_hrefs(start_url)

    asyncio.run(main(links))
    print(get_folder_size('images'))
