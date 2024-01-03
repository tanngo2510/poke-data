import csv
import abc


class Entity(metaclass=abc.ABCMeta):
    def __init__(self, id, name_en, name_hans, name_hant, name_jp):
        self.id = id
        self.name_en = name_en
        self.name_hans = name_hans
        self.name_hant = name_hant
        self.name_jp = name_jp

    def __str__(self):
        return f"{self.id}, {self.name_en}, {self.name_hans}, {self.name_hant}, {self.name_jp}"

    def to_list(self):
        return [self.id, self.name_en, self.name_hans, self.name_hant, self.name_jp]

    @staticmethod
    def from_list(lst):
        return Entity(lst[0], lst[1], lst[2], lst[3], lst[4])

    @staticmethod
    def read_from_csv(file_name):
        entities = []
        with open(file_name, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)
            for row in reader:
                entities.append(Entity.from_list(row))
        return entities

    @staticmethod
    def write_to_csv(file_name, entities, header=["id", "name_en", "name_hans", "name_hant", "name_jp"]):
        with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            for entity in entities:
                writer.writerow(entity.to_list())
