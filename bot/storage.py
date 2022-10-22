import json
from bot.entity import MessageRepository, PhotoRepository, Message, Photo


class Storage:
    storage_path = 'E:\\Files\\storage\\storage1.json'

    def __init__(self, messages=None, photos=None):
        if messages and photos:
            self.messages = messages
            self.photos = photos
        else:
            with open(self.storage_path, encoding='utf-8') as json_file:
                data = json.load(json_file)
                self.messages = MessageRepository(self.to_entity(Message, data['storage']['message']))
                self.photos = PhotoRepository(self.to_entity(Photo, data['storage']['photo']))

    def dumb_repositories(self):
        self.dump_any_repositories(self.messages, self.photos, self.storage_path)

    @staticmethod
    def to_entity(cls_, iterable):
        return [cls_().from_json(element) for element in iterable]

    @staticmethod
    def dump_any_repositories(messages: MessageRepository, photos: PhotoRepository, storage_path: str):
        with open(storage_path, 'w') as storage_file:
            storage_dict = {
                "storage": {
                    **messages.get_json(),
                    **photos.get_json()}
            }
            json.dump(storage_dict, storage_file, ensure_ascii=True)


class UpdateStorage:
    def __init__(self, new_storage: Storage, old_storage: Storage):
        self.new_storage: Storage = new_storage
        self.old_storage: Storage = old_storage

    def merge(self):
        result_messages = self.get_merged_repository(
            self.new_storage.messages.entities,
            self.old_storage.messages.entities,
            'text'
        )
        result_photos = self.get_merged_repository(
            self.new_storage.photos.entities,
            self.old_storage.photos.entities,
            'path'
        )
        return Storage(
            MessageRepository(result_messages),
            PhotoRepository(result_photos)
        )

    @staticmethod
    def get_merged_repository(new, old, key):
        values_from_key = [element.__dict__[key] for element in old]
        unique_elements = [element for element in new if element.__dict__[key] not in values_from_key]
        result = old + unique_elements
        return result
