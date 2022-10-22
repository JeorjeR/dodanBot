import os
import telebot

from bot.domain.exceptions import DodanException
from bot.domain.storage.storage import Storage, init_storage
from bot.web.post_services import get_post_content
from bot.web.utilites import create_markup, logging_message

bot: telebot.TeleBot = telebot.TeleBot(os.environ['ACCESS_TOKEN'])  # create telegram bot
storage: Storage = init_storage()  # init storage


def start_bot():
    """starting bot"""
    try:
        bot.infinity_polling(none_stop=True, interval=0)
    finally:
        bot.send_message(int(os.environ['MY_ID']), 'Я домой, я в тильте')
        storage.dumb_repositories()


@bot.message_handler(content_types=['text'])
def process_message(message):
    markup = create_markup(message)  # Создаем кнопки
    logging_message(bot, message)  # Логируем сообщение
    # Создаем пост
    if message.text == 'Шындарахнуть':
        bot.send_photo(
            chat_id=os.environ['CHAT_ID'],
            **get_post_content(storage)
        )
        bot.send_message(message.chat.id, 'Кого шындарахнули?!', reply_markup=markup)
    elif message.text == 'Обновить':
        if message.chat.id == int(os.environ['MY_ID']):
            from bot.domain.storage.update_storage import update_storage
            update_storage()
            bot.send_message(message.chat.id, 'Я обновился нах!', reply_markup=markup)
    elif message.text == 'Инициализировать':
        if message.chat.id == int(os.environ['MY_ID']):
            from bot.domain.storage.storage_init import set_storage
            set_storage()
            bot.send_message(message.chat.id, 'Иницивнвлиавв...!', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Я командос Четкий нах!', reply_markup=markup)
