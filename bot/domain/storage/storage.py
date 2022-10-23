import json
import os

from bot.domain.objects.repository import RepositoryFactory, Repository


def storage_empty_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except json.decoder.JSONDecodeError:
            from bot.domain.storage.storage_init import set_storage
            set_storage()
            return func(*args, **kwargs)
    return wrapper


class Storage:
    storage_path = os.environ['STORAGE_PATH']

    def __init__(self, *, json_storage):
        for name_repository, json_repository in json_storage['storage'].items():
            self.__dict__[name_repository] = self.create_repository_from_json(name_repository, json_repository)

    def get_photos(self) -> Repository:
        return self.__dict__['photo']

    def get_messages(self) -> Repository:
        return self.__dict__['message']

    def get_names_of_repository(self) -> list:
        return list(self.__dict__.keys())

    def get_repository(self, repository_name: str) -> Repository:
        return self.__dict__[repository_name]

    @staticmethod
    def get_repository_pk(repository_name: str) -> str:
        if repository_name == 'message':
            return 'text'
        else:
            return 'path'

    @staticmethod
    def create_repository_from_json(name_repository: str, json_repository: list[dict]) -> Repository:
        return RepositoryFactory.get_repository(name_repository)(json_repository)

    def dumb_repositories(self) -> None:
        self.dump_any_repositories(*self.__dict__.values())

    @staticmethod
    def dump_any_repositories(*repositories) -> None:
        with open(Storage.storage_path, 'w') as storage_file:
            storage_dict = {
                "storage": dict(
                    repository.get_json() for repository in repositories
                )
            }
            json.dump(storage_dict, storage_file)

    @staticmethod
    def get_json_storage() -> dict:
        with open(Storage.storage_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


@storage_empty_exception
def init_storage() -> Storage:
    json_storage: dict = Storage.get_json_storage()
    storage: Storage = Storage(json_storage=json_storage)
    return storage
