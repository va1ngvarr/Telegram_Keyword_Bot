from bot.database.models import Words, Channels, Recipients


def delete_word(word):
    instance = Words.get_or_none(word=rf"{word}")
    if instance:
        instance.delete_instance()


def delete_channel(channel):
    instance = Channels.get_or_none(channel=channel)
    if instance:
        instance.delete_instance()


def delete_recipient(link):
    instance = Recipients.get_or_none(user=link)
    if instance:
        instance.delete_instance()
