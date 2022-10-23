import os

from bot.domain.storage.storage import Storage


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


def get_new_storage() -> Storage:
    return Storage(
        json_storage={
            'storage': {
                'message': get_messages(),
                'photo': get_photos()
            }
        }
    )


def set_storage() -> None:
    storage: Storage = get_new_storage()
    storage.dumb_repositories()
