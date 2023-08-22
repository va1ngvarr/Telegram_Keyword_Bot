from bot.database.models import Words, Channels, Recipients


def get_words():
    words = Words.filter()
    list_word: list = []
    for word in words:
        list_word.append(word.word)

    return list_word


def get_channels():
    channels = Channels.filter()
    list_channels: list = []
    for channel in channels:
        list_channels.append(channel.channel)

    return list_channels


def get_recipients():
    users = Recipients.filter()
    list_users: list = []
    for user in users:
        list_users.append(user.user)

    return list_users
