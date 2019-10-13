from typing import Optional, List

from .formatter import format_dict

__all__ = [
    'Character',
    'to_natives',
    'from_natives'
]


class Character:
    name: str
    skill: Optional[str]
    stat: Optional[str]
    flowers: List[str]
    favourite_gifts: List[str]
    disliked_gifts: List[str]
    lost_items: List[str]
    house: Optional[str]

    def __init__(self, name):
        self.name = name
        self.skill = None
        self.stat = None
        self.flowers = []
        self.favourite_gifts = []
        self.disliked_gifts = []
        self.lost_items = []
        self.house = None

    def __repr__(self):
        return f"Character({', '.join(format_dict(self.__dict__))})"

    def to_native(self) -> dict:
        return self.__dict__

    @staticmethod
    def from_native(character_dict: dict) -> 'Character':
        character = Character(None)
        character.__dict__ = character_dict
        return character


def to_natives(characters: List[Character]) -> List[dict]:
    character_list = []
    for character in characters:
        character_list.append(character.to_native())
    return character_list


def from_natives(characters: List[dict]) -> List[Character]:
    character_list = []
    for character_dict in characters:
        character_list.append(Character.from_native(character_dict))
    return character_list
