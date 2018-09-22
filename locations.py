import random
import utility


class Loc:
    def __init__(self, name, desc):
        self.name = name
        self.raw_desc = desc
        self.desc = ''
        self.gen_names()

    def gen_names(self):
        """Generates names to access later during gameplay"""
        self.desc = self.raw_desc.format(name=utility.get_rand_name())

    def __str__(self):
        return self.desc

    def __repr__(self):
        return f"Loc(name='{self.name}', desc='{self.raw_desc}')"


class Locations:
    def __init__(self, generate=True):
        self._locs = []
        if generate:
            for i in range(10):
                self.add_rand_loc()

    def __getattr__(self, item):
        """Gets Loc obj from _locs list if available"""
        for loc in self._locs:
            if loc.name == item:
                return loc
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def add_loc(self, name, desc):
        self._locs.append(Loc(name, desc))

    def add_rand_loc(self) -> Loc:
        templates = {
            "city_of": "the City of {name}",
            "cave": "cave {name}",
            "valley": "{name} Valley",
            "village": "{name} Village",
            "town": "{name}town",
            "river": "{name} river",
            "lake": "{name} lake",
        }
        rand_name, rand_desc = random.choice(list(templates.items()))
        loc = Loc(rand_name, rand_desc)
        self._locs.append(loc)
        return loc

    def get_rand(self) -> Loc:
        """ Returns random Loc obj from _locs list"""
        return random.choice(self._locs)

    def get_rand_str(self) -> str:
        return self.get_rand().desc
