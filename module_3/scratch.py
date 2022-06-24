'''
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}


response = requests.get(url='http://httpbin.org/user-agent', headers=headers)
print(response.text)
'''

'''
from fake_useragent import UserAgent
import requests

url = 'http://httpbin.org/user-agent'

for _ in range(10):
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)
'''

import requests

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'

response = requests.get(url=url, stream=True)
with open('file1.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=10000):
        video.write(piece)




