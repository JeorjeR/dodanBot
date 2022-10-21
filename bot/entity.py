from typing import Union


class Message:
    def __init__(self, path: str, usable: bool, text: str):
        self.text: str = text
        self.path: str = path
        self.usable: bool = usable

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "usable": self.usable,
            "text": self.text
        }

    @staticmethod
    def from_json(message_dict: dict):
        return Message(
            path=message_dict['path'],
            usable=message_dict['usable'],
            text=message_dict['text']
        )


class Photo:
    def __init__(self, path: str, usable: bool):
        self.path: str = path
        self.usable: bool = usable

    def get_file(self):
        return open(self.path[:-1], 'rb')

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "usable": self.usable,
        }

    @staticmethod
    def from_json(photo_dict: dict):
        return Photo(
            path=photo_dict['path'],
            usable=photo_dict['usable'],
        )


class MessageRepository:

    def __init__(self, iterable: list[Union[dict, Message]]):
        self.messages = [Message.from_json(message) for message in iterable]

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_json(self) -> dict:
        return {
            "message": [message.to_dict() for message in self.messages]
        }

    def make_all_useless(self):
        for message in self.messages:
            message.usable = False


class PhotoRepository:

    def __init__(self, iterable: list[dict]):
        self.photos = [Photo.from_json(photo) for photo in iterable]

    def add_photo(self, photo: Photo):
        self.photos.append(photo)

    def get_json(self) -> dict:
        return {
            "photo": [photo.to_dict() for photo in self.photos]
        }

    def make_all_useless(self):
        for message in self.photos:
            message.usable = False
