from __future__ import annotations

from functools import partial

import format_templates as ft
import utility


class Command:
    def __init__(self, user_split_input: list, player=utility._debug_player):
        self.player = player
        self.user_input = user_split_input
        self.func_format = ft.FuncFormat(self.player)
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
                self.func_format.display('movement', direction=value)
                return
        print(ft.temps['invalid'])


class AttackCommand(Command):
    def _run(self):
        pass  # TODO: Implement entity target by name


class WaitCommand(Command):
    def _run(self):
        self.func_format.display('wait')


class LookCommand(Command):
    def _run(self):
        self.func_format.display('look')


class DebugCommand(Command):
    def _run(self):
        self.func_format.display('invalid')


class CMDInput:
    cmds_dict = {
        ("move", "go", "step"): MoveCommand,
        ("attack", "hit"): AttackCommand,
        ("skip", "wait", "."): WaitCommand,
        ("look", "see", "inspect"): LookCommand,
        ("debug",): DebugCommand
    }

    @classmethod
    def get(cls, k, default=None):
        return cls.cmds_dict.get(k, default)

    def __init__(self, player, default_prompt="> "):
        self.prompt = default_prompt
        self.player = player

    def __call__(self):
        self.text = input(self.prompt)
        self.input_cmds = self.text.split(' ')
        self._parse()

    def _parse(self):
        for keywords, command in self.cmds_dict.items():
            if self.input_cmds[0] in keywords:
                command(self.input_cmds, self.player)
                return
        print("Invalid input")


def _test():

    while True:
        cmd = CMDInput(utility._debug_player)
        cmd()


if __name__ == '__main__':
    _test()
