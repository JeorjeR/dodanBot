import os

from telebot import types, TeleBot
from telebot.types import Message, User


def create_markup(message) -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup()
    commands: list[types.KeyboardButton] = [types.KeyboardButton('Шындарахнуть')]
    if message.chat.id == int(os.environ['MY_ID']):
        commands += [
            types.KeyboardButton('Обновить'),
            types.KeyboardButton('Инициализировать')
        ]
    markup.add(*commands)
    return markup


def get_user_from_message(message: Message) -> str:
    user: User = message.from_user
    if user.full_name:
        user_full_name: str = user.full_name
    else:
        user_full_name: str = f'{user.first_name} {user.last_name}'
    user_information: str = f'From User: \n\t\t\t{user_full_name}\n\t\t\tID:{user.id}\n\t\t\tusername:{user.username}\n'
    message_text: str = f'Text of message: \n>\n{message.text}\n<'
    return f'{user_information}\n{message_text}'


def logging_message(bot: TeleBot, message: Message) -> None:
    import datetime
    bot.send_message(
        os.environ['LOG_ID'],
        f'{get_user_from_message(message)}\nDate of log: {datetime.datetime.now():%H:%M %d.%m.%Y}'
    )
