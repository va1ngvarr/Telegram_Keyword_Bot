from telethon import TelegramClient

import re, logging

from bot.database.methods.get import get_words
from bot import client


cache = ""


async def new_channels_messages_regex_handler(event):
    global cache
    get_message = event.raw_text.lower()
    get_chat = await event.get_chat()
    get_sender = await event.get_sender()
    if get_message != cache:
        if get_message.count("\n") < 3:
            for word in get_words():
                match = re.search(rf"{word}", get_message)
                if match:
                    for link in get_senders():
                        await client.forward_messages(link, event.message)
                        await client.send_message(
                            link,
                            f"Chat - @{get_chat.username}\n"
                            f"User - @{get_sender.username}",
                        )
                    cache = get_message
                    break
