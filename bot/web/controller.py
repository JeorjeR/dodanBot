import os
import telebot
from telebot import types
from bot.web.post_services import get_post_content

bot: telebot.TeleBot = telebot.TeleBot(os.environ['ACCESS_TOKEN'])  # create telegram bot


def start_bot():
    """starting bot"""
    bot.infinity_polling(none_stop=True, interval=0)


@bot.message_handler(commands=['Шындарахнуть'])
def send_post(message):
    # Создаем пост
    bot.send_photo(
        chat_id=os.environ['CHAT_ID'],
        **get_post_content()
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.ReplyKeyboardMarkup()
    command = types.KeyboardButton('/Шындарахнуть')
    markup.add(command)
    bot.send_message(message.chat.id, 'Я командос Четкий нах!', reply_markup=markup)
