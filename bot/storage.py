import json
import os
from bot.repository import RepositoryFactory


class Storage:
    storage_path = os.environ['STORAGE_PATH']

    def __init__(self, *, json_storage):
        for name_repository, json_repository in json_storage['storage'].items():
            self.__dict__[name_repository] = self.create_repository_from_json(name_repository, json_repository)

    def get_photos(self):
        return self.__dict__['photo']

    def get_messages(self):
        return self.__dict__['message']

    @staticmethod
    def create_repository_from_json(name_repository: str, json_repository: list[dict]):
        return RepositoryFactory.get_repository(name_repository)(json_repository)

    def dumb_repositories(self):
        self.dump_any_repositories(*self.__dict__.values())

    @staticmethod
    def dump_any_repositories(*repositories):
        with open(Storage.storage_path, 'w') as storage_file:
            storage_dict = {
                "storage": dict(
                    repository.get_json() for repository in repositories
                )
            }
            json.dump(storage_dict, storage_file, ensure_ascii=True)

    @staticmethod
    def get_json_storage() -> dict:
        with open(Storage.storage_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def init_storage() -> Storage:
    json_storage: dict = Storage.get_json_storage()
    storage: Storage = Storage(json_storage=json_storage)
    return storage
