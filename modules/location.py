from modules.entity import Entity
import csv


class Location(Entity):
    def __init__(self, id, region_id, name_en, name_hans, name_hant, name_jp):
        super().__init__(id, name_en, name_hans, name_hant, name_jp)
        self.region_id = region_id

    def to_list(self):
        return [self.id, self.region_id, self.name_en, self.name_hans, self.name_hant, self.name_jp]

    @staticmethod
    def from_list(lst):
        return Location(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5])

    @staticmethod
    def read_from_csv(file_name):
        locations = []
        with open(file_name, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)
            for row in reader:
                locations.append(Location.from_list(row))
        return locations
