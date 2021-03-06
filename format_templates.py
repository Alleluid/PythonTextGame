import json
import os
import random
from string import Formatter
from types import SimpleNamespace

from utility import get_rand_name
from game_classes.base import Consts
from locations import Loc, Locations

with open(os.path.abspath("resources/templates.json"), encoding='utf-8') as f:
    # Strings are broken up by line to be more readable in JSON, this joins them with newlines.
    temps = {key: '\n'.join(str_list) for key, str_list in json.load(f).items()}


class FuncFormat(Formatter):

    def __init__(self, player):
        self.player = player

    def convert_field(self, value, conversion):
        if conversion == 'f':
            try:
                return value(value)
            except TypeError:
                return value()
        else:
            return super().convert_field(value, conversion)

    def display(self, string_key, **kwargs):
        string = temps[string_key]
        print(self.format(string, **kwargs))


class Random:

    @staticmethod
    def name():
        return get_rand_name()


def _test():
    ff = FuncFormat()
    player = SimpleNamespace(name="TEST NAME")

    welcome = ff.format(temps['welcome'], random=Random, player=player)
    print(welcome)


if __name__ == '__main__':
    _test()
