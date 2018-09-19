from __future__ import annotations

from functools import partial

import format_templates as ft
import utility

ff = ft.FuncFormat()


class Command:
    def __init__(self, user_input: list):
        self.user_input = user_input
        self._run()

    def _run(self):
        raise NotImplementedError


class MoveCommand(Command):
    def _run(self):
        directions = {
            ("north", "up", "forward"): "north",
            ("east", "right"): "east",
            ("south", "down", "backward"): "south",
            ("west", "left"): "west",
        }

        for keywords, value in directions.items():
            if self.user_input[1] in keywords:
                ft.func_format_print(ff, 'movement', player=utility._debug_player, direction=value)
                return
        print(ft.temps['invalid'])


class Commands:
    cmds = {
        ("move", "go", "step"): MoveCommand,
        ("attack", "hit"): partial(print, "attacked"),
        ("skip", "wait", "."): partial(print, "waited"),
        ("look", "see", "inspect"): partial(print, "looked"),
    }

    @classmethod
    def get(cls, k, default=None):
        return cls.cmds.get(k, default)


def _test():

    while True:
        prompt = input("> ")
        user_input = prompt.split()

        for keywords, cmd in Commands.cmds.items():
            if user_input[0] in keywords:
                cmd(user_input)


if __name__ == '__main__':
    _test()
