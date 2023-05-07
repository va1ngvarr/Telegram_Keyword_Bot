from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

from bot import client


async def join_channel(channel):
    try:
        await client(JoinChannelRequest(channel))
        return f"Successfully joined a channel: {channel}"
    except:
        return f"Failed to join a channel: {channel}"


async def leave_channel(channel):
    try:
        await client(LeaveChannelRequest(channel))
        return f"Successfully leaved a channel: {channel}"
    except:
        return f"Failed to leave a channel: {channel}"


def regex_func(input_string):
    input_list = input_string.split(",")
    regex_phrases = []

    pass_phrase = "([\\s\\S]+?)"

    for phrase in input_list:
        parts = phrase.split()
        if len(parts) > 1:
            regex_phrase = (
                rf"({pass_phrase.join(['(' + part + ')' for part in parts])})"
            )
        else:
            regex_phrase = rf"{parts[0]}+?"
        regex_phrases.append(regex_phrase)

    return regex_phrases
