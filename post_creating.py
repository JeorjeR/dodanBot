import os
import random
from telebot import TeleBot
from bot.entity import MessageRepository, PhotoRepository, Message, Photo
from bot.storage import Storage, UpdateStorage
from test import get_new_storage


def get_message(messages: MessageRepository):
    """Method for generate str"""
    useless_messages = [message for message in messages.messages if not message.usable]
    if not useless_messages:
        messages.make_all_useless()
        message: Message = random.choice(messages.messages)
    else:
        message: Message = random.choice(useless_messages)
    message.usable = True
    return message.text


def get_photo(photos: PhotoRepository):
    """Method for get path to photo"""
    useless_photos = [photo for photo in photos.photos if not photo.usable]
    if not useless_photos:
        photos.make_all_useless()
        photo: Photo = random.choice(photos.photos)
    else:
        photo: Photo = random.choice(useless_photos)
    photo.usable = True
    return photo.get_file()


def create_post(bot: TeleBot):
    # Инициализируем и обновляем хранилище, есди появились новые данные
    old_storage: Storage = Storage()
    new_storage: Storage = get_new_storage()
    storage: Storage = UpdateStorage(new_storage, old_storage).merge()
    bot.send_photo(
        chat_id=os.environ['CHAT_ID'],
        photo=get_photo(storage.photos),
        caption=get_message(storage.messages)
    )
    storage.dumb_repositories()
