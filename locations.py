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
    _locs = [
        Loc("plains", "the plains"),
        Loc("forest", "the forest"),
        Loc("tundra", "the tundra"),

        Loc("city_of", "the city of {name}"),
        Loc("city", "{name} City"),
        Loc("lake", "lake {name}"),
        Loc("valley", "{name} valley"),
        Loc("river", "{name} river"),
        Loc("cave_of", "the cave of {name}"),
        Loc("cave", "cave {name}"),
    ]

    def __init__(self):
        pass

    def __getattr__(self, item):
        """Gets Loc obj from _locs list if available"""
        for loc in self._locs:
            if loc.name == item:
                return loc
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def rand(self) -> Loc:
        """ Returns random Loc obj from _locs list"""
        return random.choice(self._locs)

    def rand_str(self) -> str:
        return self.rand().desc
