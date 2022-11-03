from telethon import TelegramClient, sync
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.environ.get('ID')
api_hash = os.environ.get('HASH')

client = TelegramClient('task_1', api_id, api_hash)
client.start()

participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')
names = [' '.join([x.first_name, x.last_name]) for x in participants
         if all(i is not None for i in (x.first_name, x.last_name))]
print(names)
