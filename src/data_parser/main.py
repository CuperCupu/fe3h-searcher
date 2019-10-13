import argparse
import json

import pandas as pd

from data import characters, items
from .characters_parser import parse_character_sheet
from .items_parser import aggregate_items


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("target")
    return parser.parse_args()


def parse_characters(data):
    character_sheet = data.parse('Character', header=None)
    return parse_character_sheet(character_sheet)


def main():
    args = parse_args()
    data = pd.ExcelFile(args.file)
    parsed_characters = parse_characters(data)
    parsed_items = aggregate_items(parsed_characters)
    to_save = {
        'characters': characters.to_natives(parsed_characters),
        'items': items.to_natives(parsed_items)
    }
    with open(args.target, 'w') as f:
        json.dump(to_save, f, indent=4)
