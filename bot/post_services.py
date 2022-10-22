import random
from typing import Union
from bot.entity import Message, Photo
from bot.repository import Repository
from bot.storage import Storage, init_storage


def get_entity(repository: Repository):
    useless_entity = [entity for entity in repository.entities if not entity.usable]
    if not useless_entity:
        repository.make_all_useless()
        entity: Union[Photo, Message] = random.choice(repository.entities)
    else:
        entity: Union[Photo, Message] = random.choice(useless_entity)
    entity.usable = True
    return entity.get_content()


def get_post_content():
    storage: Storage = init_storage()
    # Инициализируем и обновляем хранилище, есди появились новые данные
    # TODO нужны дескрипторы для доступа к репозиториям
    post = {
        'photo': get_entity(storage.get_photos()),
        'caption': get_entity(storage.get_messages())
    }
    storage.dumb_repositories()
    return post
