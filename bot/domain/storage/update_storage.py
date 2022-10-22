from dotenv import load_dotenv
from bot.domain.objects.repository import  Repository
from bot.domain.storage.storage import Storage, init_storage
from bot.domain.storage.storage_init import get_new_storage

load_dotenv()


class UpdateStorage:
    def __init__(self, new_storage: Storage, old_storage: Storage):
        self.new_storage: Storage = new_storage
        self.old_storage: Storage = old_storage

    def merge(self):
        return Storage(
            json_storage={
                'storage': dict(
                    self.get_merged_repository(
                        self.new_storage.get_repository(repository_name),
                        self.old_storage.get_repository(repository_name),
                        Storage.get_repository_pk(repository_name)
                    ).get_json() for repository_name in self.new_storage.get_names_of_repository()
                )
            }
        )

    @staticmethod
    def get_merged_repository(new: Repository, old: Repository, key: str):
        values_from_key = [element.__dict__[key] for element in old.entities]
        unique_elements = [element for element in new.entities if element.__dict__[key] not in values_from_key]
        # TODO описать метод присоединения к репозитори списка
        old.add_entities(unique_elements)
        return old


def update_storage():
    old_storage: Storage = init_storage()
    new_storage: Storage = get_new_storage()
    storage: Storage = UpdateStorage(new_storage, old_storage).merge()
    storage.dumb_repositories()

