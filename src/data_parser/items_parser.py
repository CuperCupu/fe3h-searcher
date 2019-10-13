from typing import List

from data.characters import Character
from data.items import Item


def aggregate_items(characters: List[Character]):
    items = {}

    def get_item(name):
        if name not in items:
            item = Item(name)
            items[name] = item
            return item
        else:
            return items[name]

    for character in characters:
        for item_name in character.flowers:
            item = get_item(item_name)
            item.liked_by.append(character.name)
        for item_name in character.favourite_gifts:
            item = get_item(item_name)
            item.liked_by.append(character.name)
        for item_name in character.disliked_gifts:
            item = get_item(item_name)
            item.disliked_by.append(character.name)
        for item_name in character.lost_items:
            item = get_item(item_name)
            item.lost_by.append(character.name)

    return list(items.values())
