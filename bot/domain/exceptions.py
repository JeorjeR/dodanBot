from telebot import TeleBot


class DodanException(Exception):
    def __init__(self, bot: TeleBot):
        self.bot = bot

    def __str__(self):
        self.bot.send_message("I'm so sorry! I'm Dodan and can't fulfill your request")
        return "I'm so sorry! I'm Dodan and can't fulfill your request"

