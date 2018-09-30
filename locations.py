import json
import os
import random
import utility


class Loc:
    """
    Object to store a game location.

    Usually randomly generated from name list. Can be gotten directly by name.

    """
    def __init__(self, name, desc):
        self.name = name
        self.raw_desc = desc
        self.desc = ''
        self.gen_names()

    def gen_names(self):
        """
        Generates names to access later during gameplay.
        """
        self.desc = self.raw_desc.format(name=utility.get_rand_name())

    def __str__(self):
        return self.desc

    def __repr__(self):
        return f"Loc(name='{self.name}', desc='{self.raw_desc}')"


class Locations:
    def __init__(self, generate=True):
        self.locs = []
        if generate:
            for i in range(20):
                self.add_rand_loc()

    def __getattr__(self, item):
        """
        Gets Loc obj from locs list if available
        """
        for loc in self.locs:
            if loc.name == item:
                return loc
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def add_loc(self, name, desc):
        self.locs.append(Loc(name, desc))

    def add_rand_loc(self) -> Loc:
        templates = json.load(os.path.abspath("resources/location_templates.json"))
        rand_name, rand_desc = random.choice(list(templates.items()))
        loc = Loc(rand_name, rand_desc)
        self.locs.append(loc)
        return loc

    def get_rand(self) -> Loc:
        """
        Returns random Loc obj from locs list
        """
        return random.choice(self.locs)

    def get_rand_str(self) -> str:
        return self.get_rand().desc
