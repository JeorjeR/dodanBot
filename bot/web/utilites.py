import os

from telebot import types


def create_markup(message):
    markup = types.ReplyKeyboardMarkup()
    commands = [types.KeyboardButton('Шындарахнуть')]
    if message.chat.id == int(os.environ['MY_ID']):
        commands += [
            types.KeyboardButton('Обновить')
        ]
    markup.add(*commands)
    return markup
