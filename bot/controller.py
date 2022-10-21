import os
import telebot
from telebot import types
from post_creating import create_post

bot: telebot.TeleBot = telebot.TeleBot(os.environ['ACCESS_TOKEN'])  # create telegram bot


def start_bot():
    """starting bot"""
    bot.infinity_polling(none_stop=True, interval=0)


@bot.message_handler(commands=['Шындарахнуть'])
def send_post(message):
    # Создаем пост
    create_post(bot)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.ReplyKeyboardMarkup()
    command = types.KeyboardButton('/Шындарахнуть')
    markup.add(command)
    bot.send_message(message.chat.id, 'Я командос Четкий нах!', reply_markup=markup)
