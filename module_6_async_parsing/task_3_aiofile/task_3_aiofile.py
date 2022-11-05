import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup
import requests
import asyncio
import aiofiles


domain = 'https://parsinger.ru/asyncio/aiofile/2/'


def get_img_urls(url: str) -> list[str]:
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    links = [x.text for x in soup.find_all('a', class_='lnk_img')]
    links = [domain + link for link in links]

    return links


async def get_img(session, url, name_img)