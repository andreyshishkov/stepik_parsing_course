from telethon import TelegramClient, sync, events, connection
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'

with TelegramClient('task_1', api_id, api_hash) as client:
    messages = client.iter_messages(group)
    addition = 0
    for message in messages:
        message_ = message.message
        if message_:
            addition += int(message_)
print(addition)
