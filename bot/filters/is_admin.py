from aiogram.dispatcher.filters import Filter
from aiogram.types import Message, CallbackQuery

from bot import config


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, *args) -> bool:
        if type(args[0]) == Message:
            message: Message = args[0]
            return str(message.from_user.id) in config.ADMIN_LIST

        elif type(args[0]) == CallbackQuery:
            callback: CallbackQuery = args[0]
            return str(callback.from_user.id) in config.ADMIN_LIST
