class Entity:
    def __init__(self, *, json_entity: dict):
        for key, value in json_entity.items():
            self.__dict__[key] = value

    def to_dict(self) -> dict:
        return{
            f"{attr}": value for attr, value in self.__dict__.items()
        }

    def from_json(self, entity_dict: dict):
        self.__init__(
            **{attr: entity_dict[attr] for attr in entity_dict}
        )
        return self


class Message(Entity):
    def get_content(self):
        return self.__dict__['text']


class Photo(Entity):
    def get_content(self):
        return open(self.__dict__['path'], 'rb')
