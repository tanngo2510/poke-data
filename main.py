import os
from modules.pokemon import Pokemon

PATH_CSV = os.path.join(os.path.dirname(__file__), "csv")

list_pokemon = Pokemon.read_from_csv(os.path.join(PATH_CSV, "pokemon.csv"))
