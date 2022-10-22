from bot.domain.storage.storage import Storage, init_storage
from bot.domain.storage.storage_init import get_new_storage


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


def update_storage():
    old_storage: Storage = init_storage()
    new_storage: Storage = Storage(**get_new_storage())
    storage: Storage = UpdateStorage(new_storage, old_storage).merge()
