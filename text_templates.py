import re


class StrTemp:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return self.string

    def callable_format(self, **kwargs) -> str:
        """ `.format()` but if callable is passed will call it for each occurrence."""

        # `re.sub` passes a re.match object to it's repl() call, so this is to ignore that.
        def remove_args(func):
            def wrapper(*args):
                return func()
            return wrapper

        for keyword, value in kwargs.items():
            # Compiles regex obj for slightly better efficiency.
            # Old-style '%' formatting used due to importance of curly braces here.
            re_keyword = re.compile('<%s>' % keyword, re.MULTILINE)

            if callable(value):
                noarg_val = remove_args(value)
            else:
                noarg_val = value

            self.string = re.sub(re_keyword, noarg_val, self.string)

        return self.string

    def template_print(self, **kwargs):
        print(self.callable_format(**kwargs))


class Templates:
    def __init__(self, player_name):
        self.player = player_name

        self.welcome = \
f"""Welcome to the world of <rand_name>!
Here you, {self.player}, will experience some stuff I guess!
Explore wonderous locations such as: 
<rand_location>,
<rand_location>,
<rand_location>,
and <rand_location>!
"""
        self.welcome = StrTemp(self.welcome)

        self.invalid = \
"""Invalid input.
"""
        self.invalid = StrTemp(self.invalid)

        self.encounter = \
f"""A wild beast named <rand_name> attacks you {self.player}!
What will you do?
"""
        self.encounter = StrTemp(self.encounter)

        self.movement = \
f"""{self.player} moves towards the <direction>.
"""
        self.movement = StrTemp(self.movement)