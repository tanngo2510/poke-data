import requests
import csv
import os

BASE_URI = "https://pokeapi.co/api/v2"
LIMIT = 99999


def crawl_skills():
    url = f"{BASE_URI}/move?limit={LIMIT}"
    res = requests.get(url)
    res = res.json()
    os.system("cls")
    count = res["count"]
    data = res["results"]
    for index in range(count):
        print(f"> Skill #{
              index + 1}/{count} [{round(((index + 1) * 100 / count), 2)}%]", end="\r")
        sub_res = requests.get(data[index]["url"])
        sub_res = sub_res.json()
        skill_id = sub_res["id"]
        names = sub_res["names"]
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


def crawl_items(from_id=1):
    url = f"{BASE_URI}/item?limit={LIMIT}"
    res = requests.get(url)
    res = res.json()

    count = res["count"]
    data = res["results"]
    for index in range(from_id - 1, count):
        os.system("cls")
        print(f"> Searching item: #{
              index + 1}/{count} [{round(((index + 1) * 100 / count), 2)}%]")
        sub_url = data[index]["url"]
        sub_res = requests.get(sub_url)
        sub_res = sub_res.json()
        item_id = sub_res["id"]
        names = sub_res["names"]
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
            print(f"> Found sprite for item: {index + 1}")
            filename = sub_res["name"]
            with open(f"../sprites/item/{filename}.png", "wb") as img:
                response = requests.get(sprite, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    img.write(block)


crawl_skills()
crawl_items()
