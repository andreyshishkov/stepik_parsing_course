from telethon import TelegramClient, sync, events, connection
from telethon.tl.functions.users import GetFullUserRequest
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ.get('ID'))
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'
lst = [5125814085, 5423813689, 5395359919, 5330282124, 5451738743, 5319101536,
       5599808192, 5552200609, 5560704798, 5421516684, 5596049016, 5313438049,
       5530400713, 5595171770, 5373895551, 5582701295, 5401839698, 5443556002,
       5445202221, 5394891665, 5486227453, 5342098799, 5486370067, 5576022537,
       5539803054, 5523594628, 5449816597, 5235694206]

with TelegramClient('task_5', api_id, api_hash) as client:
    users = client.iter_participants(group)
    amount = 0
    for user in users:
        info = client(GetFullUserRequest(user)).full_user
        user_id = info.id
        if (user_id in lst) and info.about:
            amount += int(info.about)
    print(amount)
