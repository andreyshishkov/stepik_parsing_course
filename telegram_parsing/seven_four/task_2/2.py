from telethon import TelegramClient, sync
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')

client = TelegramClient('task_2', api_id, api_hash)
client.start()

participants = client.get_participants('https://t.me/Parsinger_Telethon_Test')

contacts = []
for participant in participants:
    contact = (str(participant.id), participant.first_name,
               participant.last_name, participant.phone)
    if all(contact):
        contacts.append(' '.join(contact))

print(contacts)
