import requests

for i in range(1, 161):
    with open(f'image{i}.png', 'wb') as file:
        response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')
        image = response.content
        file.write(image)
