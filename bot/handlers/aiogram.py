import os, sys, sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from telethon import TelegramClient
from bot.database import register_all_models
from bot.database.methods.create import add_new_channel, add_new_word, add_new_recipient
from bot.database.methods.delete import delete_channel, delete_word, delete_recipient
from bot.database.methods.get import get_channels, get_words, get_recipients
from bot.database.models import Words, conn
from bot.keyboards.reply import (
    get_admin_keyboard,
    get_cancel_kb,
    get_cancel_kb_super,
    get_cancel_kb_super_2,
)
from bot.utils import regex_func, join_channel, leave_channel
from bot.misc.states import (
    PurgeDataBase,
    CreateWords,
    DeleteWords,
    CreateChannels,
    DeleteChannels,
    CreateRecipients,
    DeleteRecipients,
)


async def start_handler(message: Message):
    await message.answer("Welcome to the bot!", reply_markup=get_admin_keyboard())


async def main_manu_handler(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Here's main menu", reply_markup=get_admin_keyboard())


async def bot_reload(message: Message):
    await message.answer("Bot is reloading", reply_markup=get_admin_keyboard())
    python = sys.executable
    os.execl(python, python, *sys.argv)


async def purge_db_handler(message: Message):
    await message.answer(
        "Are you sure to purge the database?",
        reply_markup=get_cancel_kb_super(),
    )
    await PurgeDataBase.first()


async def clean_db(message: Message, state: FSMContext):
    for channel in get_channels():
        await leave_channel(channel)
    conn.close()
    os.remove("sqlite3.db")
    register_all_models()
    await message.answer(
        "Database was cleaned and new was initialized",
        reply_markup=get_admin_keyboard(),
    )
    await state.finish()


# === WORDS ==============================================================

# add


async def add_words_handler(message: Message):
    await message.answer(
        "Type the words, separated by commas, which you want to add",
        reply_markup=get_cancel_kb(),
    )
    await CreateWords.first()


async def new_words(message: Message, state: FSMContext):
    for word in regex_func(message.text):
        add_new_word(word)
    await message.answer("Words were added!", reply_markup=get_admin_keyboard())
    await state.finish()


# delete


async def delete_words_handler(message: Message):
    await message.answer(
        "Type the words, separated by commas, which you want to delete or delete everything",
        reply_markup=get_cancel_kb_super_2(),
    )
    await DeleteWords.first()


async def delete_all_words(message: Message, state: FSMContext):
    for word in get_words():
        delete_word(word)
    await message.answer("Words were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


async def delete_words(message: Message, state: FSMContext):
    for word in message.text.split(","):
        delete_word(word)
    await message.answer("Words were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


# get


async def get_words_handler(message: Message):
    words = get_words()
    if len(words) > 0:
        await message.answer(words)
    else:
        await message.answer("There are no added words!")


# === CHANNELS =========================================================

# add


async def add_channels_handler(message: Message):
    await message.answer(
        "Type the links to channels, separated by commas, which you want to add",
        reply_markup=get_cancel_kb(),
    )
    await CreateChannels.first()


async def new_channels(message: Message, state: FSMContext):
    for channel in message.text.replace(" ", "").split(","):
        add_new_channel(channel)
        await message.answer(await join_channel(channel))

    await message.answer("Channels were added!", reply_markup=get_admin_keyboard())
    await state.finish()


# delete


async def delete_channels_handler(message: Message):
    await message.answer(
        "Type the links to channels, separated by commas, which you want to delete or delete everything",
        reply_markup=get_cancel_kb_super_2(),
    )
    await DeleteChannels().first()


async def delete_all_channels(message: Message, state: FSMContext):
    for channel in get_channels():
        delete_channel(channel)
        await message.answer(await leave_channel(channel))
    await message.answer("Channels were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


async def delete_channels(message: Message, state: FSMContext):
    for channel in message.text.replace(" ", "").split(","):
        delete_channel(channel)
        await message.answer(await leave_channel(channel))
    await message.answer("Channels were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


# get


async def get_channels_handler(message: Message):
    channels = get_channels()
    if len(channels) > 0:
        await message.answer(channels)
    else:
        await message.answer("There are no added channels!")


# === SENDERS ===========================================================

# add


async def add_recipients_handler(message: Message, state: FSMContext):
    await message.answer(
        "Type the links to recipients, separated by commas, which you want to add",
        reply_markup=get_cancel_kb(),
    )
    await CreateRecipients.first()


async def new_recipients(message: Message, state: FSMContext):
    for recipient in message.text.replace(" ", "").split(","):
        add_new_recipient(recipient)
    await message.answer("Recipients were added!", reply_markup=get_admin_keyboard())
    await state.finish()


# delete


async def delete_recipients_handler(message: Message):
    await message.answer(
        "Type the links to recipients, separated by commas, which you want to delete or delete everything",
        reply_markup=get_cancel_kb_super_2(),
    )
    await DeleteRecipients().first()


async def delete_all_recipients(message: Message, state: FSMContext):
    for recipient in get_recipients():
        delete_recipients(recipient)
    await message.answer("Recipients were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


async def delete_recipients(message: Message, state: FSMContext):
    for recipient in message.text.replace(" ", "").split(","):
        delete_recipient(recipient)
    await message.answer("Recipients were deleted!", reply_markup=get_admin_keyboard())
    await state.finish()


# get


async def get_recipients_handler(message: Message):
    recipients = get_recipients()
    if len(recipients) > 0:
        await message.answer(recipients)
    else:
        await message.answer("There are no added recipients!")
