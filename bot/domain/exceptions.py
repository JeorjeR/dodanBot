import os

from telebot import TeleBot


class DodanException(Exception):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def __str__(self):
        self.bot.send_message(os.environ['LOG_ID'], "I'm so sorry! I'm Dodan and can't fulfill your request")


