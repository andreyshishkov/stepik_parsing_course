from telethon import TelegramClient, sync, events, connection
from telethon.tl.types import InputMessagesFilterPinned
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'

with TelegramClient('task_2', api_id, api_hash) as client:
    pinned_message = client.get_messages(group, filter=InputMessagesFilterPinned)[0]
    user_id = pinned_message.from_id.user_id
print(user_id)
