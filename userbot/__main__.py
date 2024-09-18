from pyrogram import Client, filters
from pyrogram.handlers import message_handler
from pyrogram.types import Message, ChatMember
import datetime
import random
import string
from dotenv import load_dotenv
import os 

load_dotenv()



client = Client('my_account', api_hash=os.getenv('API_HASH'), api_id=os.getenv('API_ID'))

target_chat_id = os.getenv('target_chat_id')
channel_id = os.getenv('channel_id')

@client.on_message(filters.chat(int(target_chat_id)))
async def echo(client: Client, message: Message):
    print(text)
    text = message.text
    try:
        if 'Token' in text and 'MCap' in text:
            await client.forward_messages(chat_id=channel_id, from_chat_id=message.chat.id, message_ids=message.id)
    except:
        pass
    
        

    
client.run()