import requests

for i in range(1, 501):
    url = f'http://parsinger.ru/task/1/{i}.html'
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.text)
        break