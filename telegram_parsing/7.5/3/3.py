from telethon import TelegramClient, sync, events, connection
from dotenv import load_dotenv
import os

load_dotenv()
api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'
user_id = 5330282124

with TelegramClient('task_3', api_id, api_hash) as client:
    messages = client.iter_messages(group)
    acc = 0
    for message in messages:
        if message.from_id and message.from_id.user_id == user_id:
            try:
                acc += int(message.message)
            except ValueError:
                pass
print(acc)
