from telethon import TelegramClient, sync, connection, events
from telethon.tl.types import InputMessagesFilterPhotos
from dotenv import load_dotenv
from shutil import rmtree
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'

os.mkdir('data')

with TelegramClient('task_7.5.5', api_id, api_hash) as client:
    messages = client.iter_messages(group, filter=InputMessagesFilterPhotos, limit=100)
    for i, message in enumerate(messages):
        client.download_media(message, f'data/{i}')


def get_directory_path(path):
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


print(get_directory_path('data'))
rmtree('data')
