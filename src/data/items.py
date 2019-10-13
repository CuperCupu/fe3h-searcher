from typing import List

from .formatter import format_dict

__all__ = [
    'Item',
    'to_natives',
    'from_natives'
]


class Item:

    def __init__(self, name):
        self.name = name
        self.liked_by = []
        self.disliked_by = []
        self.lost_by = []

    def __repr__(self):
        return f"Item({', '.join(format_dict(self.__dict__))})"

    def to_native(self) -> dict:
        return self.__dict__

    @staticmethod
    def from_native(item_dict: dict) -> 'Item':
        item = Item(None)
        item.__dict__ = item_dict
        return item


def to_natives(items: List[Item]) -> List[dict]:
    item_list = []
    for item in items:
        item_list.append(item.to_native())
    return item_list


def from_natives(items: List[dict]) -> List[Item]:
    item_list = []
    for item_dict in items:
        item_list.append(Item.from_native(item_dict))
    return item_list
