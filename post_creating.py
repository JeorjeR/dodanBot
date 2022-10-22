import os
import random
from typing import Union
from telebot import TeleBot
from bot.entity import MessageRepository, PhotoRepository, Message, Photo
from bot.storage import Storage, UpdateStorage
from test import get_new_storage


def get_entity(repository: Union[MessageRepository, PhotoRepository]):
    useless_entity = [entity for entity in repository.entities if not entity.usable]
    if not useless_entity:
        repository.make_all_useless()
        entity: Union[Photo, Message] = random.choice(repository.entities)
    else:
        entity: Union[Photo, Message] = random.choice(useless_entity)
    entity.usable = True
    return entity.get_content()


def create_post(bot: TeleBot):
    # Инициализируем и обновляем хранилище, есди появились новые данные
    old_storage: Storage = Storage()
    new_storage: Storage = get_new_storage()
    storage: Storage = UpdateStorage(new_storage, old_storage).merge()
    bot.send_photo(
        chat_id=os.environ['CHAT_ID'],
        photo=get_entity(storage.photos),
        caption=get_entity(storage.messages)
    )
    storage.dumb_repositories()
