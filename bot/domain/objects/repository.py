from bot.domain.objects.entity import Entity, Photo, Message


class Repository:
    name = "entity"
    entity_class = Entity

    def __init__(self, json_repository: list[dict]):
        self.entities = self.create_repository_from_json(json_repository)

    def get_json(self):
        return self.name, [entity.to_dict() for entity in self.entities]

    def make_all_useless(self):
        for entity in self.entities:
            entity.usable = False

    def create_repository_from_json(self, json_repository: list[dict]):
        return [self.entity_class(json_entity=entity) for entity in json_repository]


class RepositoryFactory:
    @staticmethod
    def get_repository(name_repository):
        if name_repository == 'message':
            # TODO дожга вызываться функция которая вернет обект репозитория созданного класса
            cls_ = type(
                'MessageRepository',
                (Repository,),
                {'name': name_repository, 'entity_class': Message}
            )
        elif name_repository == 'photo':
            cls_ = type(
                'PhotoRepository',
                (Repository,),
                {'name': name_repository, 'entity_class': Photo}
            )
        else:
            cls_ = Repository
        return cls_
