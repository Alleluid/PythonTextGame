import json
import os
import random
from types import SimpleNamespace

from utility import FuncFormat, get_rand_name

with open(os.path.abspath("resources/templates.json"), encoding='utf-8') as f:
    # Strings are broken up by line to be more readable in JSON, this joins them with newlines.
    temps = {key: '\n'.join(str_list) for key, str_list in json.load(f).items()}


def func_format_print(ff: FuncFormat, string_key, **kwargs):
    string = temps[string_key]
    print(ff.format(string, **kwargs))


class Random:
    @staticmethod
    def location():
        return random.choice((
            f"Lake {get_rand_name()}",
            f"City of {get_rand_name()}",
            f"{get_rand_name()} City",
            f"Great {get_rand_name()} Mountains",
        ))

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
