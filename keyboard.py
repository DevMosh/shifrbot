from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_menu():
    button_1 = KeyboardButton(text='🔐')
    button_2 = KeyboardButton(text='🔓')
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])
    return keyboard


def shifr_menu():
    button_back = KeyboardButton(text='🔙 Назад')
    button_1 = KeyboardButton(text='Цезарь')
    button_2 = KeyboardButton(text='Виженера')
    button_3 = KeyboardButton(text='Атбаш')
    button_4 = KeyboardButton(text='Трисемиус')
    button_5 = KeyboardButton(text='Полибианский квадрат')
    button_6 = KeyboardButton(text='Биграмный')
    button_7 = KeyboardButton(text='Гронсфельда')

    keyboard = ReplyKeyboardMarkup(keyboard=[[button_back],
                                             [button_1, button_2],
                                             [button_3, button_4],
                                             [button_5],
                                             [button_6, button_7]])
    return keyboard
