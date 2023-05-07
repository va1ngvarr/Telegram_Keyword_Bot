from aiogram import Dispatcher
from telethon import TelegramClient, events

from bot.filters import IsAdmin
from bot.database.methods.get import get_channels

from .aiogram import *
from .telethon import *


def register_telethon_handlers(client: TelegramClient):
    client.add_event_handler(
        new_channels_messages_regex_handler,
        events.NewMessage(incoming=True, chats=get_channels()),
    )


def register_aiogram_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, IsAdmin(), state="*", commands=["start"])

    dp.register_message_handler(
        main_manu_handler,
        IsAdmin(),
        content_types=["text"],
        text="🏠 Go to main menu",
        state="*",
    )

    dp.register_message_handler(
        bot_reload,
        IsAdmin(),
        content_types=["text"],
        text="Reload the bot",
        state="*",
    )

    dp.register_message_handler(
        purge_db_handler,
        IsAdmin(),
        content_types=["text"],
        text="Purge the database🧨",
        state="*",
    )

    dp.register_message_handler(
        clean_db,
        content_types=["text"],
        text="Yes, purge the database🧨",
        state=PurgeDataBase.purge,
    )

    # === WORDS ==============================================================

    # add

    dp.register_message_handler(
        add_words_handler,
        IsAdmin(),
        content_types=["text"],
        text="Add words",
        state="*",
    )

    dp.register_message_handler(
        new_words, content_types=["text"], state=CreateWords.words
    )

    # delete

    dp.register_message_handler(
        delete_words_handler,
        IsAdmin(),
        content_types=["text"],
        text="Delete words",
        state="*",
    )

    dp.register_message_handler(
        delete_all_words,
        content_types=["text"],
        text="Delete everything🧨",
        state=DeleteWords.words,
    )

    dp.register_message_handler(
        delete_words, content_types=["text"], state=DeleteWords.words
    )

    # get

    dp.register_message_handler(
        get_words_handler,
        IsAdmin(),
        content_types=["text"],
        text="Get words",
        state="*",
    )

    # === CHANNELS =========================================================

    # add

    dp.register_message_handler(
        add_channels_handler,
        IsAdmin(),
        content_types=["text"],
        text="Add channels",
        state="*",
    )

    dp.register_message_handler(
        new_channels,
        content_types=["text"],
        state=CreateChannels.channels,
    )

    # delete

    dp.register_message_handler(
        delete_channels_handler,
        IsAdmin(),
        content_types=["text"],
        text="Delete channels",
        state="*",
    )

    dp.register_message_handler(
        delete_all_channels,
        content_types=["text"],
        text="Delete everything🧨",
        state=DeleteChannels.channels,
    )

    dp.register_message_handler(
        delete_channels,
        content_types=["text"],
        state=DeleteChannels.channels,
    )

    # get

    dp.register_message_handler(
        get_channels_handler,
        IsAdmin(),
        content_types=["text"],
        text="Get channels",
        state="*",
    )

    # === RECIPIENTS ===========================================================

    # add

    dp.register_message_handler(
        add_recipients_handler,
        IsAdmin(),
        content_types=["text"],
        text="Add recipients",
        state="*",
    )

    dp.register_message_handler(
        new_recipients, IsAdmin(), content_types=["text"], state=CreateRecipients.users
    )

    # delete

    dp.register_message_handler(
        delete_recipients_handler,
        IsAdmin(),
        content_types=["text"],
        text="Delete recipients",
        state="*",
    )

    dp.register_message_handler(
        delete_all_recipients,
        content_types=["text"],
        text="Delete everything🧨",
        state=DeleteRecipients.users,
    )

    dp.register_message_handler(
        delete_recipients,
        content_types=["text"],
        state=DeleteRecipients.users,
    )

    # get

    dp.register_message_handler(
        get_recipients_handler,
        IsAdmin(),
        content_types=["text"],
        text="Get recipients",
        state="*",
    )
