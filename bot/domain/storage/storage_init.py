import os
from bot.domain.objects.repository import Repository
from bot.domain.storage.storage import Storage


class MessageRepository(Repository):
    name = "message"


class PhotoRepository(Repository):
    name = "photo"


def get_messages() -> list[dict]:
    file_path = os.environ['ORIGIN_MESSAGE_PATH']
    with open(file_path, 'r', encoding='windows-1251') as messages_file:
        message = ''
        messages = []
        for element in messages_file:
            if element != '\n':
                message += element
            else:
                messages.append(
                    dict(
                        path=file_path,
                        usable=False,
                        text=message)
                )
                message = ''
        return messages


def get_photos() -> list[dict]:
    directory_path = os.environ['ORIGIN_PHOTO_PATH']
    photos = os.listdir(directory_path)
    photos = [
        dict(
            path=f'{directory_path}\\{photo}',
            usable=False
        ) for photo in photos
    ]
    return photos


def get_new_storage():
    messages_repository: MessageRepository = MessageRepository(get_messages())
    photo_repository: PhotoRepository = PhotoRepository(get_photos())
    Storage.dump_any_repositories(messages_repository, photo_repository)
    return {
        'messages': messages_repository,
        'photos': photo_repository
    }


if __name__ == '__main__':
    get_new_storage()

    # new_storage: Storage = Storage(**get_new_storage())
    # storage: Storage = UpdateStorage(new_storage, old_storage).merge()

            # self.messages = MessageRepository(self.to_entity(Message, data['storage']['message']))
            # self.photos = PhotoRepository(self.to_entity(Photo, data['storage']['photo']))


# class UpdateStorage:
#     def __init__(self, new_storage: Storage, old_storage: Storage):
#         self.new_storage: Storage = new_storage
#         self.old_storage: Storage = old_storage
#
#     def merge(self):
#         result_messages = self.get_merged_repository(
#             self.new_storage.messages.entities,
#             self.old_storage.messages.entities,
#             'text'
#         )
#         result_photos = self.get_merged_repository(
#             self.new_storage.photos.entities,
#             self.old_storage.photos.entities,
#             'path'
#         )
#         return Storage(
#             MessageRepository(result_messages),
#             PhotoRepository(result_photos)
#         )
#
#     @staticmethod
#     def get_merged_repository(new, old, key):
#         values_from_key = [element.__dict__[key] for element in old]
#         unique_elements = [element for element in new if element.__dict__[key] not in values_from_key]
#         result = old + unique_elements
#         return result
