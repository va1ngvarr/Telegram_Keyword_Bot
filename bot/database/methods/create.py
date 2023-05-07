from bot.database.models import Words, Channels, Recipients


def add_new_word(phrases):
    if not Words.get_or_none(word=phrases):
        Words.create(word=phrases)


def add_new_channel(channel):
    if not Channels.get_or_none(channel=channel):
        Channels.create(channel=channel)


def add_new_recipient(link):
    if not Recipients.get_or_none(user=link):
        Recipients.create(user=link)
