from bot.domain.objects.entity import Entity, Photo, Message


class Repository:
    name = "entity"
    entity_class = Entity

    def __init__(self, json_repository: list[dict]):
        self.entities = self.create_repository_from_json(json_repository)

    def get_json(self) -> tuple[str, list]:
        return self.name, [entity.to_dict() for entity in self.entities]

    def make_all_useless(self) -> None:
        for entity in self.entities:
            entity.usable = False

    def create_repository_from_json(self, json_repository: list[dict]) -> list[entity_class]:
        return [self.entity_class(json_entity=entity) for entity in json_repository]

    def add_entities(self, entities_list: list[entity_class]) -> None:
        self.entities += entities_list


class RepositoryFactory:
    @staticmethod
    def get_repository(name_repository) -> type:
        if name_repository == 'message':
            cls_: type = type(
                'MessageRepository',
                (Repository,),
                {'name': name_repository, 'entity_class': Message}
            )
        elif name_repository == 'photo':
            cls_: type = type(
                'PhotoRepository',
                (Repository,),
                {'name': name_repository, 'entity_class': Photo}
            )
        else:
            cls_: type = Repository
        return cls_
