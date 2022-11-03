from telethon import TelegramClient, sync, events, connection
from telethon.tl.functions.users import GetFullUserRequest
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.environ.get('ID')
api_hash = os.environ.get('HASH')
group = 'https://t.me/Parsinger_Telethon_Test'
lst = ['William_Price34', 'Nancy_Montgomery54', 'Gloria_Thompson4', 'Linda_Hernandez4', 'Nathan_King43',
       'Thomas_Jones56', 'Sara_Martin434', 'Elizabeth_Weber', 'Joshua_Andrews34',
       'Erica_Moore34', 'Nancy_Johnson3', 'Mildred_James', 'Brian_Johnson2',
       'James_Washington3', 'Richard_Welch', 'Scott_Stevenson32', 'Mark_Mendez980', 'Lisa_Hawkins']

with TelegramClient('task_6', api_id, api_hash) as client:
    users = client.iter_participants(group)
    amount = 0
    for user in users:
        user_info = client(GetFullUserRequest(user)).full_user
        if user.username in lst:
            amount += int(user_info.about)
    print(amount)
