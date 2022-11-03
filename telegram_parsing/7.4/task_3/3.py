from telethon import TelegramClient, sync, events, connection
from dotenv import load_dotenv
import os
import shutil

load_dotenv()
os.mkdir('photos')


api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'


with TelegramClient('task_3', api_id, api_hash) as client:
    participants = client.get_participants(group)
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f"photos/{i}")


def get_directory_path(path):
    size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


print(get_directory_path('photos'))
shutil.rmtree('photos')
