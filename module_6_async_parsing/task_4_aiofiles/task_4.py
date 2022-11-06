import aiohttp
import aiofiles
import asyncio
from bs4 import BeautifulSoup
import requests
import os


unique_images = set()


def get_folder_size(dir_name):
    size = 0
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


async def get_image(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}.jpg', mode='wb') as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await file.write(x)


def get_image_hrefs(html: str):
    """find links to images on current url"""
    soup = BeautifulSoup(html, 'lxml')
    image_links = [x['src'] for x in soup.find_all('img', class_='picture')]
    return image_links


async def get_images_from_url(session: aiohttp.client.ClientSession, url: str):
    async with session.get(url) as response:
        resp = await response.text()
        image_links = get_image_hrefs(resp)

        tasks = []
        for link in image_links:
            link_name = hash(link)
            if link_name not in unique_images:
                task = asyncio.create_task(get_image(session, link, link_name))
                tasks.append(task)
                unique_images.add(link_name)
        await asyncio.gather(*tasks)


async def get_urls2images(session: aiohttp.client.ClientSession, link: str):
    domain = 'https://parsinger.ru/asyncio/aiofile/3/depth2/'
    async with session.get(link) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')

            links = [x['href'] for x in soup.find_all('a', class_='lnk_img')]
            links = [domain + link for link in links]

        tasks = []
        for link in links:
            task = asyncio.create_task(get_images_from_url(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def main(links: list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in links:
            task = asyncio.create_task(get_urls2images(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


def get_urls2urls(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    domain = 'https://parsinger.ru/asyncio/aiofile/3/'
    links = [x['href'] for x in soup.find_all('a', class_='lnk_img')]
    links = [domain + link for link in links]
    return links


if __name__ == '__main__':
    start_url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'
    first_depth_urls = get_urls2urls(start_url)
    asyncio.run(main(first_depth_urls))

    result = get_folder_size('images')
    print('Size of folder is', result)
