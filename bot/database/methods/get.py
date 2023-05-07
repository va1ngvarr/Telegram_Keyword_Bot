from bot.database.models import Words, Channels, Recipients


def get_words():
    words = Words.filter()
    list_word: list = []
    for word in words:
        list_word.append(word.word)

    return list_word


def get_channels():
    words = Channels.filter()
    list_channels: list = []
    for word in words:
        list_channels.append(word.channel)

    return list_channels


def get_recipients():
    users = Recipients.filter()
    list_users: list = []
    for word in users:
        list_users.append(word.user)

    return list_users
