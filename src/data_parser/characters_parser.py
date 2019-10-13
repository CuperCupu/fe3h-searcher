from pandas import DataFrame, Series

from data.characters import Character
from data import houses

sequential_house = [
    houses.black_eagles,
    houses.blue_lions,
    houses.golden_deers,
    houses.church_of_seiros,
    houses.knights_of_seiros
]


def parse_character_sheet(sheet: DataFrame):
    sheet = sheet.drop([0, 1])
    characters = []
    house_idx = 0
    for index, row in sheet.iterrows():
        if isinstance(row[1], str):
            characters.append(parse_character(row, sequential_house[house_idx]))
        else:
            house_idx += 1
    return characters


def parse_string(string):
    if not isinstance(string, str):
        return None
    return string.strip().replace('\u2019', "'")


def parse_list(cell):
    if isinstance(cell, str):
        return [parse_string(x) for x in cell.split('\n') if x != '-']
    return []


def parse_character(row: Series, house):
    name = row[1]
    if not name:
        raise ValueError("Invalid row")
    character = Character(row[1])
    character.house = house
    skill = parse_string(row[2])
    if skill != '-':
        character.skill = skill
    stat = parse_string(row[3])
    if stat != '-':
        character.stat = stat
    flowers = parse_list(row[4])
    if flowers:
        character.flowers = flowers
    favourite_gifts = parse_list(row[5])
    if favourite_gifts:
        character.favourite_gifts.extend(favourite_gifts)
    disliked_gifts = parse_list(row[6])
    if disliked_gifts:
        character.disliked_gifts.extend(disliked_gifts)
    lost_items = parse_list(row[7])
    if lost_items:
        character.lost_items.extend(lost_items)
    return character
