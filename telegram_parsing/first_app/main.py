from telethon import TelegramClient, events, sync, connection
from config import ID, HASH


api_id = ID # Тут укажите полученый ранее api
api_hash = HASH # Тут укажите полученый ранее hash

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print(client.get_me())
client.disconnect()
