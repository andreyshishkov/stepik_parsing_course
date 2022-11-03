from telethon import TelegramClient, sync, connection, events
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'

with TelegramClient('task_7.5.4', api_id, api_hash) as client:
    messages = client.iter_messages(group)
    usernames = set()
    for message in messages:
        if message.from_id:
            user_id = message.from_id.user_id
            if user_id:
                username = client.get_entity(user_id).username
                usernames.add(username)

usernames = list(usernames)
print(usernames)
