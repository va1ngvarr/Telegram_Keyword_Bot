# KeyWord_Bot
This bot tracks added keywords in added channels or groups, then it forwards messages with keywords to added recipients. Keywords by adding have transform to regex-patterns. And keywords, which have more than 1 word have a especial separate, so if words from the same keyword are came across not a nearby in message, it's anyway compatible with pattern

## How to use
At first, just set your own values in **bot/config.py**
### How it works
It has two parts. Client and Bot. Bot has only admin panel, so that's availible only who there is in admin-list at **bot/config.py**. Admin panel is necessary to manage data (add/delete channels, words, recipients).
Client is user account. Client automatically joins to added channels and forwards some messages to recipients
### What to do next
Run **main.py**
Script's going to ask user account's password, then bot token or phone number(and pin-code). Don't give him bot token! Otherwise user side will be performing user side work. It isn't convenient, because bots have some restrictions. Next remains only to add data through your bot and get messages from user account.

There you go!
