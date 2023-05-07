from aiogram.dispatcher.filters.state import StatesGroup, State


class PurgeDataBase(StatesGroup):
    purge = State()


class CreateWords(StatesGroup):
    words = State()


class DeleteWords(StatesGroup):
    words = State()


class CreateChannels(StatesGroup):
    channels = State()


class DeleteChannels(StatesGroup):
    channels = State()


class CreateRecipients(StatesGroup):
    users = State()


class DeleteRecipients(StatesGroup):
    users = State()
