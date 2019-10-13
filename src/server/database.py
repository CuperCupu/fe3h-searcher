import json
from typing import Union, TypeVar, Generic, List, Tuple

from Levenshtein import distance

from data.characters import Character, from_natives as ch_from_natives
from data.items import Item, from_natives as it_from_natives

T = TypeVar('T')

infinite = float('inf')


class SearchableString:

    def __init__(self, text):
        self.text = text
        self.texts = text.lower().split()
        self.count = len(self.texts)
        self.excess = [0 for _ in self.texts]
        for idx, text in enumerate(self.texts):
            for i in range(len(self.texts)):
                if idx != i:
                    self.excess[i] += len(text)
        for i, value in enumerate(self.excess):
            self.excess[i] = value / 10

    @staticmethod
    def score(source, dest, excess):
        if len(dest) < len(source):
            return None
        if source in dest:
            return (len(dest) - len(source)) / 2 + excess
        else:
            return (distance(dest, source) + excess) * 2

    def __call__(self, querystring):
        lowest = infinite
        iter_count = self.count - len(querystring)
        if iter_count < 0:
            return lowest
        for i in range(iter_count + 1):
            score = 0
            for idx, (source, dest) in enumerate(zip(querystring, self.texts[i:])):
                scored = self.score(source, dest, self.excess[idx])
                if scored:
                    score += scored
                else:
                    score = infinite
                    continue
            if lowest > score:
                lowest = score
        return lowest


class Index(Generic[T]):

    def __init__(self, data, name='name'):
        self.data: List[Tuple[SearchableString, T]] = []
        for item in data:
            self.data.append((SearchableString(getattr(item, name)), item))

    def search(self, querystring) -> List[Tuple[float, T]]:
        result = []
        for name, data in self.data:
            score = name(querystring)
            result.append((score, data))
        return result


class Database:

    def __init__(self, filename='data.json'):
        with open(filename) as f:
            data = json.load(f)
        self.characters = ch_from_natives(data['characters'])
        self.items = it_from_natives(data['items'])

        self._characters_index: Index[Character] = Index(self.characters)
        self._items_index: Index[Item] = Index(self.items)

    @staticmethod
    def preprocess_querystring(querystring) -> str:
        return querystring.strip().lower().split()

    def search(self, querystring) -> List[Tuple[float, Union[Character, Item]]]:
        querystring = self.preprocess_querystring(querystring)
        characters = self._characters_index.search(querystring)
        items = self._items_index.search(querystring)
        result = characters + items
        result.sort(key=lambda x: x[0])
        return result

    def search_characters(self, querystring) -> List[Tuple[float, Character]]:
        querystring = self.preprocess_querystring(querystring)
        result = self._characters_index.search(querystring)
        result.sort(key=lambda x: x[0])
        return result

    def search_items(self, querystring) -> List[Tuple[float, Item]]:
        querystring = self.preprocess_querystring(querystring)
        result = self._items_index.search(querystring)
        result.sort(key=lambda x: x[0])
        return result

