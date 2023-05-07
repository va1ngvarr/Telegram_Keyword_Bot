from telethon import TelegramClient
from bot import config

client = TelegramClient(
    "client+" + str(config.PHONE_NUMBER), config.API_KEY, config.API_HASH
)
