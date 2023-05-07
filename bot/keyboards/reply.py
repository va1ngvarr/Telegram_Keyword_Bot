from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_admin_keyboard():
    admin_rmk = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = KeyboardButton(text="Add channels")
    btn_2 = KeyboardButton(text="Delete channels")
    btn_3 = KeyboardButton(text="Get channels")
    btn_4 = KeyboardButton(text="Add words")
    btn_5 = KeyboardButton(text="Delete words")
    btn_6 = KeyboardButton(text="Get words")
    btn_7 = KeyboardButton(text="Add recipients")
    btn_8 = KeyboardButton(text="Delete recipients")
    btn_9 = KeyboardButton(text="Get recipients")
    btn_10 = KeyboardButton(text="Reload the bot")
    btn_11 = KeyboardButton(text="Purge the database🧨")
    admin_rmk.add(btn_1, btn_2, btn_3)
    admin_rmk.row()
    admin_rmk.add(btn_4, btn_5, btn_6)
    admin_rmk.row()
    admin_rmk.add(btn_7, btn_8, btn_9)
    admin_rmk.row()
    admin_rmk.add(btn_10, btn_11)
    return admin_rmk


def get_cancel_kb():
    rmk = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = KeyboardButton(text="🏠 Go to main menu")
    rmk.add(menu_btn)
    return rmk


def get_cancel_kb_super():
    rmk = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = KeyboardButton(text="🏠 Go to main menu")
    btn = KeyboardButton(text="Yes, purge the database🧨")
    rmk.add(menu_btn)
    rmk.row()
    rmk.add(btn)
    return rmk


def get_cancel_kb_super_2():
    rmk = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_btn = KeyboardButton(text="🏠 Go to main menu")
    btn = KeyboardButton(text="Delete everything🧨")
    rmk.add(menu_btn)
    rmk.row()
    rmk.add(btn)
    return rmk
