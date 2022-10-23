import random

from bot.domain.objects.repository import Repository
from bot.domain.storage.storage import Storage


def get_entity(repository: Repository):
    useless_entity: list[repository.entity_class] = [entity for entity in repository.entities if not entity.usable]
    print(f'{repository.__class__.__name__} --> {len(useless_entity)}')
    if not useless_entity:
        repository.make_all_useless()
        entity: [repository.entity_class] = random.choice(repository.entities)
    else:
        entity: [repository.entity_class] = random.choice(useless_entity)
    entity.usable = True
    return entity.get_content()


def get_post_content(storage: Storage) -> dict:
    post = {
        'photo': get_entity(storage.get_photos()),
        'caption': get_entity(storage.get_messages())
    }
    return post
