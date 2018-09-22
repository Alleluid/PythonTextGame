import os
import random
from string import Formatter

from types import SimpleNamespace

# DEBUG
_debug_player = SimpleNamespace(name="DEBUG PLAYER")


def get_rand_name(count=1):
    with open(os.path.abspath("resources/names.txt"), encoding='utf-8') as f:
        names = f.readlines()
    if count == 1:
        return random.choice(names).strip()
    else:
        return [get_rand_name() for _ in range(count)]




if __name__ == '__main__':
    some_names = get_rand_name()
    print(some_names)
