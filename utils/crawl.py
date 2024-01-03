import requests
import csv
import os
import json
from alive_progress import alive_bar

BASE_URI = "https://pokeapi.co/api/v2"
LIMIT = 99999


def crawl_skills():
    with open("../csv/skills.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["skill_id", "name_en", "name_hans", "name_hant", "name_jp"])
    url = f"{BASE_URI}/move?limit={LIMIT}"
    res = requests.get(url)
    res = res.json()
    count = res["count"]
    data = res["results"]
    with alive_bar(count) as bar:
        for index in range(count):
            sub_res = requests.get(data[index]["url"])
            sub_res = sub_res.json()
            skill_id = sub_res["id"]
            names = sub_res["names"]
            hant = ""
            hans = ""
            en = ""
            jp = ""
            for name in names:
                if name["language"]["name"] == "zh-Hant":
                    hant = name["name"]
                if name["language"]["name"] == "zh-Hans":
                    hans = name["name"]
                if name["language"]["name"] == "en":
                    en = name["name"]
                if name["language"]["name"] == "ja-Hrkt":
                    jp = name["name"]

            with open("../csv/skills.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([skill_id, en, hans, hant, jp])
            bar()


def crawl_regions():
    with open("../csv/regions.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["region_id", "name_en", "name_hans", "name_hant", "name_jp"])
    url = f"{BASE_URI}/region?limit={LIMIT}"
    res = requests.get(url)
    res = res.json()
    count = res["count"]
    data = res["results"]
    with alive_bar(count) as bar:
        for index in range(count):
            sub_url = data[index]["url"]
            sub_res = requests.get(sub_url)
            sub_res = sub_res.json()
            region_id = sub_res["id"]
            names = sub_res["names"]
            hant = ""
            hans = ""
            en = ""
            jp = ""
            for name in names:
                if name["language"]["name"] == "zh-Hant":
                    hant = name["name"]
                if name["language"]["name"] == "zh-Hans":
                    hans = name["name"]
                if name["language"]["name"] == "en":
                    en = name["name"]
                if name["language"]["name"] == "ja-Hrkt":
                    jp = name["name"]

            with open("../csv/regions.csv", "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([region_id, en, hans, hant, jp])

            bar()


def crawl_items():
    with open("../csv/items.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["item_id", "name_en", "name_hans", "name_hant", "name_jp"])
    url = f"{BASE_URI}/item?limit={LIMIT}"
    res = requests.get(url)
    res = res.json()
    no_sprites = []
    count = res["count"]
    data = res["results"]
    with alive_bar(count) as bar:
        for index in range(count):
            sub_url = data[index]["url"]
            sub_res = requests.get(sub_url)
            sub_res = sub_res.json()
            item_id = sub_res["id"]
            names = sub_res["names"]
            hant = ""
            hans = ""
            en = ""
            jp = ""
            sprite = ""
            for name in names:
                if name["language"]["name"] == "zh-Hant":
                    hant = name["name"]
                if name["language"]["name"] == "zh-Hans":
                    hans = name["name"]
                if name["language"]["name"] == "en":
                    en = name["name"]
                if name["language"]["name"] == "ja-Hrkt":
                    jp = name["name"]

            with open("../csv/items.csv", "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([item_id, en, hans, hant, jp])

            sprite = sub_res["sprites"]["default"]
            if sprite:
                filename = sub_res["name"]
                with open(f"../sprites/item/{filename}.png", "wb") as img:
                    response = requests.get(sprite, stream=True)

                    if not response.ok:
                        print(response)

                    for block in response.iter_content(1024):
                        if not block:
                            break

                        img.write(block)
            else:
                no_sprites.append({
                    "id": item_id,
                    "name": name,
                    "url": sub_url
                })

            bar()

    with open("items_not_found_sprite.json", "w", encoding="utf-8") as file:
        json.dump(no_sprites, file, indent=4)


# os.system("cls")
# print("Crawling Skills...")
# crawl_skills()
# os.system("cls")
# print("Crawling Items...")
# crawl_items()
os.system("cls")
print("Crawling Regions...")
crawl_regions()
