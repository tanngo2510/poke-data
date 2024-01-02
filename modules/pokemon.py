from modules.entity import Entity
import csv


class Pokemon(Entity):
    def __init__(self, id, species_id, name_en, name_hans, name_hant, name_jp):
        super().__init__(id, name_en, name_hans, name_hant, name_jp)
        self.species_id = species_id

    def __str__(self):
        return f"{self.id}, {self.species_id}, {self.name_en}, {self.name_hans}, {self.name_hant}, {self.name_jp}"

    def to_list(self):
        return [self.id, self.species_id, self.name_en, self.name_hans, self.name_hant, self.name_jp]

    @staticmethod
    def from_list(lst):
        return Pokemon(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5])

    @staticmethod
    def read_from_csv(file_name):
        pokemon = []
        with open(file_name, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                pokemon.append(Pokemon.from_list(row))
        return pokemon
