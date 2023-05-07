from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio, logging

from bot.filters import register_all_filters
from bot.database import register_all_models
from bot.handlers import register_aiogram_handlers, register_telethon_handlers

from bot import client, config


logging.basicConfig(level=logging.INFO)
logging.getLogger()

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_models()

    register_aiogram_handlers(dp)
    register_telethon_handlers(client)

    asyncio.create_task(client.run_until_disconnected())


def main():
    if config.DEBUG:
        # Start telethon
        client.start()

        # Start aiogram
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    else:
        # TODO: Implementation of WebHook
        # It isn't necessary, since LongPoll anyway works perfectly even in product
        pass


if __name__ == "__main__":
    main()
