class Entity:
    def __init__(self, **kwargs):
        for kwarg_key, kwarg_value in kwargs.items():
            self.__dict__[kwarg_key] = kwarg_value

    def to_dict(self) -> dict:
        return{
            f"{attr}": value for attr, value in self.__dict__.items()
        }

    def from_json(self, entity_dict: dict):
        self.__init__(
            **{attr: entity_dict[attr] for attr in self.__dict__}
        )
        return self


class Message(Entity):
    def __init__(self, **kwargs):
        if not kwargs:
            self.path = None
            self.usable = None
            self.text = None
        else:
            super().__init__(**kwargs)

    def get_content(self):
        return self.__dict__['text']


class Photo(Entity):
    def __init__(self, **kwargs):
        if not kwargs:
            self.path = None
            self.usable = None
        else:
            super().__init__(**kwargs)

    def get_content(self):
        return open(self.__dict__['path'][:-1], 'rb')


class Repository:
    name = "entity"

    def __init__(self, iterable):
        self.entities = iterable

    def get_json(self) -> dict:
        return {
            self.name: [entity.to_dict() for entity in self.entities]
        }

    def make_all_useless(self):
        for entity in self.entities:
            entity.usable = False


class MessageRepository(Repository):
    name = "message"


class PhotoRepository(Repository):
    name = "photo"
