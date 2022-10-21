import os

import chardet

from bot.entity import Message, Photo, MessageRepository, PhotoRepository
from bot.storage import Storage


def get_messages() -> list[dict]:
    file_path = 'E:\\Files\\phrases\\ss.txt'
    with open(file_path, 'r', encoding='windows-1251') as messages_file:
        # print(chardet.detect(messages_file.read()))
        message = ''
        messages = []
        for element in messages_file:
            if element != '\n':
                message += element
            else:
                messages.append(Message(
                    path=file_path,
                    usable=False,
                    text=message
                ).to_dict())
                message = ''
        return messages


def get_photos() -> list[dict]:
    directory_path = 'E:\\Files\\images'
    photos = os.listdir(directory_path)
    photos = [
        Photo(
            path=f'{directory_path}\\{photo}}}',
            usable=False
        ).to_dict() for
        photo in photos
    ]
    return photos


def get_new_storage():
    messages_repository: MessageRepository = MessageRepository(get_messages())
    photo_repository: PhotoRepository = PhotoRepository(get_photos())
    # Storage.dump_any_repositories(messages_repository, photo_repository, Storage.storage_path)
    return Storage(
        messages=messages_repository,
        photos=photo_repository
    )


if __name__ == '__main__':
    get_new_storage()
