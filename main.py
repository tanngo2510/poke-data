import os
from modules.pokemon import Pokemon
from modules.item import Item
from modules.skill import Skill
from modules.region import Region
from modules.team import Team
from modules.location import Location

COLOR = {
    "RED": "\x1b[38;5;1m",
    "GREEN": "\x1b[38;5;10m",
    "YELLOW": "\033[0;33m",
    "CYAN": "\x1b[36m",
    "MAGENTA": "\x1b[35m",
    "RESET": "\033[0m"
}

PATH_CSV = os.path.join(os.path.dirname(__file__), "csv")
BASE_SPRITE = "https://raw.githubusercontent.com/tanngo2510/poke-data/master/sprites"


def export_team(teams, have_dollar=False, have_img=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for team in teams:
        name = team.name_en.lower().replace(" ", "_")
        img = f'<img src="{BASE_SPRITE}/team/{
            name}.png" style="width:80px;height:80px;display:inline;"/> ' if have_img else ""

        if team.name_hans:
            result.append(f"{dollar}{team.name_hans}={
                          img}{team.name_en}")
        elif (not have_hant) and team.name_hant:
            result.append(f"{dollar}{team.name_hant}={
                          img}{team.name_en}")
        if have_hant:
            result.append(f"{dollar}{team.name_hant}={
                          img}{team.name_en}")

    return result


def export_pokemon(list_pkm, have_dollar=False, have_img=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for pokemon in list_pkm:
        img = f'<img src="{BASE_SPRITE}/pokemon/default/{
            pokemon.id}.png" style="width:80px;height:80px;display:inline;"/> ' if have_img else ""

        if pokemon.name_hans:
            result.append(f"{dollar}{pokemon.name_hans}={
                          img}{pokemon.name_en}")
        elif (not have_hant) and pokemon.name_hant:
            result.append(f"{dollar}{pokemon.name_hant}={
                          img}{pokemon.name_en}")
        if have_hant:
            result.append(f"{dollar}{pokemon.name_hant}={
                          img}{pokemon.name_en}")

    return result


def export_skills(skills, have_dollar=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for skill in skills:
        if skill.name_hans:
            result.append(f"{dollar}{skill.name_hans}={skill.name_en}")
        elif (not have_hant) and skill.name_hant:
            result.append(f"{dollar}{skill.name_hant}={skill.name_en}")
        if have_hant:
            result.append(f"{dollar}{skill.name_hant}={skill.name_en}")
    return result


def export_regions(regions, have_dollar=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for region in regions:
        if region.name_hans:
            result.append(f"{dollar}{region.name_hans}={region.name_en}")
        elif (not have_hant) and region.name_hant:
            result.append(f"{dollar}{region.name_hant}={region.name_en}")
        if have_hant:
            result.append(f"{dollar}{region.name_hant}={region.name_en}")
    return result


def export_locations(locations, have_dollar=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for location in locations:
        if location.name_hans:
            result.append(f"{dollar}{location.name_hans}={location.name_en}")
        elif (not have_hant) and location.name_hant:
            result.append(f"{dollar}{location.name_hant}={location.name_en}")
        if have_hant:
            result.append(f"{dollar}{location.name_hant}={location.name_en}")
    return result


def export_items(items, have_dollar=False, have_img=False, have_hant=False):
    result = []
    dollar = "$" if have_dollar else ""
    for item in items:
        name = item.name_en.lower().replace(" ", "-")
        img = f'<img src="{BASE_SPRITE}/item/{
            name}.png" style="width:50px;height:50px;display:inline;"/> ' if have_img else ""

        if item.name_hans:
            result.append(f"{dollar}{item.name_hans}={
                          img}{item.name_en}")
        elif (not have_hant) and item.name_hant:
            result.append(f"{dollar}{item.name_hant}={
                          img}{item.name_en}")
        if have_hant:
            result.append(f"{dollar}{item.name_hant}={img}{item.name_en}")

    return result


def menu():
    HAVE_DOLLAR = False
    HAVE_HANT_NAME = False
    HAVE_IMAGE = False
    HAVE_PKM_NAME = True
    HAVE_CHARACTERS_NAME = False
    HAVE_ITEMS_NAME = False
    HAVE_LOCATIONS_NAME = False
    HAVE_SKILLS_NAME = False
    HAVE_VILLAIN_TEAM = False
    HAVE_REGIONS_NAME = False
    while True:
        os.system("cls")
        print("┌─────────────────────────────────────────────┐")
        print("│                                             │")
        print(
            f"│  1 - Thêm dấu $ trước tên - {f"{COLOR["GREEN"]}Active  " if HAVE_DOLLAR else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}        │")
        print(
            f"│  2 - Thêm tên phồn thể - {f"{COLOR["GREEN"]}Active  " if HAVE_HANT_NAME else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}           │")
        print(
            f"│  3 - Thêm hình vào tên - {f"{COLOR["GREEN"]}Active  " if HAVE_IMAGE else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}           │")
        print(
            f"│  4 - Xuất tên các pokemon - {f"{COLOR["GREEN"]}Active  " if HAVE_PKM_NAME else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}        │")
        print(
            f"│  5 - Xuất tên các địa khu - {f"{COLOR["GREEN"]}Active  " if HAVE_REGIONS_NAME else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}        │")
        print(
            f"│  6 - Xuất tên các kỹ năng - {f"{COLOR["GREEN"]}Active  " if HAVE_SKILLS_NAME else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}        │")
        print(
            f"│  7 - Xuất tên các vật phẩm - {f"{COLOR["GREEN"]}Active  " if HAVE_ITEMS_NAME else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]}       │")
        print(
            f"│  8 - Xuất tên các nhân vật - {COLOR["YELLOW"]}WIP{COLOR["RESET"]}            │")
        print(
            f"│  9 - Xuất tên các nhóm phản diện - {f"{COLOR["GREEN"]}Active  " if HAVE_VILLAIN_TEAM else f"{COLOR["RED"]}Deactive"}{COLOR["RESET"]} │")
        print("│  10 - Xuất danh sách tên ra file            │")
        print("│  0 - Thoát                                  │")
        print("│                                             │")
        print("└─────────────────────────────────────────────┘")
        choice = input(">> ")
        if choice == "1":
            if HAVE_DOLLAR:
                HAVE_DOLLAR = False
            else:
                HAVE_DOLLAR = True
        elif choice == "2":
            if HAVE_HANT_NAME:
                HAVE_HANT_NAME = False
            else:
                HAVE_HANT_NAME = True
        elif choice == "3":
            if HAVE_IMAGE:
                HAVE_IMAGE = False
            else:
                HAVE_IMAGE = True
        elif choice == "4":
            if HAVE_PKM_NAME:
                HAVE_PKM_NAME = False
            else:
                HAVE_PKM_NAME = True
        elif choice == "5":
            # if HAVE_REGIONS_NAME:
            #     HAVE_REGIONS_NAME = False
            # else:
            #     HAVE_REGIONS_NAME = True
            if HAVE_LOCATIONS_NAME:
                HAVE_LOCATIONS_NAME = False
            else:
                HAVE_LOCATIONS_NAME = True
        elif choice == "6":
            if HAVE_SKILLS_NAME:
                HAVE_SKILLS_NAME = False
            else:
                HAVE_SKILLS_NAME = True
        elif choice == "7":
            if HAVE_ITEMS_NAME:
                HAVE_ITEMS_NAME = False
            else:
                HAVE_ITEMS_NAME = True
        elif choice == "8":
            if HAVE_CHARACTERS_NAME:
                HAVE_CHARACTERS_NAME = False
            else:
                HAVE_CHARACTERS_NAME = True
        elif choice == "9":
            if HAVE_VILLAIN_TEAM:
                HAVE_VILLAIN_TEAM = False
            else:
                HAVE_VILLAIN_TEAM = True
        elif choice == "10":
            '''
            ┌─────────────┐
            │   POKEMON   │
            └─────────────┘
            '''
            list_pokemon = Pokemon.read_from_csv(os.path.join(
                PATH_CSV, "pokemon.csv")) if HAVE_PKM_NAME else []
            pokemon_result = export_pokemon(
                list_pokemon, HAVE_DOLLAR, HAVE_IMAGE, HAVE_HANT_NAME)
            '''
            ┌─────────────┐
            │    ITEMS    │
            └─────────────┘
            '''
            items = Item.read_from_csv(os.path.join(
                PATH_CSV, "items.csv")) if HAVE_ITEMS_NAME else []
            items_result = export_items(
                items, HAVE_DOLLAR, HAVE_IMAGE, HAVE_HANT_NAME)
            '''
            ┌──────────────┐
            │    SKILLS    │
            └──────────────┘
            '''
            skills = Skill.read_from_csv(os.path.join(
                PATH_CSV, "skills.csv")) if HAVE_SKILLS_NAME else []
            skills_result = export_items(
                skills, HAVE_DOLLAR, HAVE_HANT_NAME)
            '''
            ┌───────────────┐
            │    REGIONS    │
            └───────────────┘
            '''
            regions = Region.read_from_csv(os.path.join(
                PATH_CSV, "regions.csv")) if HAVE_REGIONS_NAME else []
            regions_result = export_regions(
                regions, HAVE_DOLLAR, HAVE_HANT_NAME)
            '''
            ┌───────────────┐
            │   LOCATIONS   │
            └───────────────┘
            '''
            locations = Location.read_from_csv(os.path.join(
                PATH_CSV, "locations.csv")) if HAVE_LOCATIONS_NAME else []
            locations_result = export_locations(
                locations, HAVE_DOLLAR, HAVE_HANT_NAME)
            '''
            ┌─────────────────┐
            │  VILLAIN TEAMS  │
            └─────────────────┘
            '''
            teams = Team.read_from_csv(os.path.join(
                PATH_CSV, "villain_team.csv")) if HAVE_VILLAIN_TEAM else []
            teams_result = export_team(
                teams, HAVE_DOLLAR, HAVE_IMAGE, HAVE_HANT_NAME)
            with open("output.txt", "w", encoding="utf-8") as file:
                for pkm in pokemon_result:
                    file.write(pkm + "\n")
                for item in items_result:
                    file.write(item + "\n")
                for skill in skills_result:
                    file.write(skill + "\n")
                for region in regions_result:
                    file.write(region + "\n")
                for location in locations_result:
                    file.write(location + "\n")
                for team in teams_result:
                    file.write(team + "\n")

            print("DONE...")
            input("Press Enter to continue...")
        elif choice == "0":
            exit()
        else:
            continue


if __name__ == "__main__":
    menu()
