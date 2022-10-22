import os

from telebot import types, TeleBot
from telebot.types import Message, User


def create_markup(message):
    markup = types.ReplyKeyboardMarkup()
    commands = [types.KeyboardButton('Шындарахнуть')]
    if message.chat.id == int(os.environ['MY_ID']):
        commands += [
            types.KeyboardButton('Обновить'),
            types.KeyboardButton('Инициализировать')
        ]
    markup.add(*commands)
    return markup


def get_user_from_message(message: Message):
    user: User = message.from_user
    if user.full_name:
        user_full_name = user.full_name
    else:
        user_full_name = f'{user.first_name} {user.last_name}'
    user_information = f'From User: \n\t\t\t{user_full_name}\n\t\t\tID:{user.id}\n\t\t\tusername:{user.username}\n'
    message_text = f'Text of message: \n>\n{message.text}\n<'
    return f'{user_information}\n{message_text}'


def logging_message(bot: TeleBot, message: Message):
    import datetime
    user_information = get_user_from_message(message)
    date_of_log = datetime.datetime.now()
    log = f'{user_information}\nDate of log: {date_of_log:%H:%M %d.%m.%Y}'
    bot.send_message(os.environ['LOG_ID'], log)
